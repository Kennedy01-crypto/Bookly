# create a file to read env variables
from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path

# Go up one level from src to the project root
BASE_DIR = Path(__file__).resolve().parent.parent

class Settings(BaseSettings):
    # define env variables
    DATABASE_URL: str

    model_config = SettingsConfigDict(env_file= BASE_DIR / ".env", extra="ignore")


Config = Settings() #type: ignore