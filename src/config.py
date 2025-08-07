# create a file to read env variables
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # define env variables
    DATABASE_URL: str

    model_config = SettingsConfigDict(env_file= ".env", extra="ignore")