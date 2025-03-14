from api.main import app  # Import FastAPI app
from mangum import Mangum  # Convert FastAPI app for Vercel

handler = Mangum(app)
