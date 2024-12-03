from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    aoc_session: str

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()
