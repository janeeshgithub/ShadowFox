import json
import time
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

app = FastAPI()


@app.get('/')
async def scrape_and_store():
    return {"Hello":"Guys"}
class URLRequest(BaseModel):
    url: str

def scrape_website(url):
    options = Options()
    options.add_argument("--headless")  # Run without opening a browser
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    try:
        driver.get(url)
        time.sleep(3)  # Wait for JavaScript content to load
        soup = BeautifulSoup(driver.page_source, "html.parser")

        data = {
            "title": soup.title.string if soup.title else "No title",
            "headings": [h.get_text(strip=True) for h in soup.find_all(["h1", "h2", "h3"])],
            "paragraphs": [p.get_text(strip=True) for p in soup.find_all("p")][:10],  # Limit to 10
            "links": [{"text": a.get_text(strip=True), "url": a["href"]} for a in soup.find_all("a", href=True)]
        }
        return data
    finally:
        driver.quit()

def save_to_json(data, filename="scraped_data.json"):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    print(f"Data saved to {filename}")

@app.post("/scrape")
async def scrape_and_store(request: URLRequest):
    scraped_data = scrape_website(request.url)
    if not scraped_data:
        raise HTTPException(status_code=400, detail="Failed to scrape the website")

    save_to_json(scraped_data)
    return {"message": "Scraping completed", "scraped_data": scraped_data}

@app.get("/scraped_data")
async def get_scraped_data():
    try:
        with open("scraped_data.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        return {"scraped_data": data}
    except FileNotFoundError:
        return {"error": "No data found. Please run the scraper first."}
