from pydantic import BaseSettings
from dotenv import load_dotenv
import os

load_dotenv()

class Settings(BaseSettings):
    PROJECT_NAME: str = os.getenv("PROJECT_NAME")
    VERSION: str = os.getenv("VERSION")
    DATABASE_URL: str = os.getenv("DATABASE_URL")
    GENAI_API_KEY: str = os.getenv("GENAI_API_KEY")

    class Config:
        env_file = ".env"  # Cargar variables de entorno desde un archivo .env

settings = Settings()