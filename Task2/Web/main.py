from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "FastAPI running on Vercel"}

@app.get("/jane")
def read_root():
    return {"message": "Jane running on Vercel"}
# Vercel requires an entry point function called "handler"
def handler(req, res):
    return app
