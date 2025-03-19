import requests
from bs4 import BeautifulSoup
import json
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
async def read_root():
    return {"message": "Hello, FastAPI on WEBSCRAP"}

class URLRequest(BaseModel):
    url: str

def scrape_website(url):
    response = requests.get(url)
    if response.status_code != 200:
        raise HTTPException(status_code=400, detail=f"Failed to retrieve page: {response.status_code}")
    
    soup = BeautifulSoup(response.text, 'html.parser')
    articles = []
    
    for item in soup.find_all('a', href=True):
        title = item.get_text(strip=True)
        link = item['href']
        
        if title and link.startswith("http"):
            articles.append({"title": title, "link": link})
    
    return articles

def save_to_json(data, filename="scrap_data.json"):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    print(f"Data saved to {filename}")

@app.post("/scrape")
async def scrape_and_store(data: URLRequest):
    scraped_data = scrape_website(data.url)
    save_to_json(scraped_data)
    return {"message": "Scraping completed", "scraped_data": scraped_data}

@app.get("/scraped_data")
async def get_scraped_data():
    try:
        with open("scrap_data.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        return {"scraped_data": data}
    except FileNotFoundError:
        return {"error": "No data found. Please run the scraper first."}



