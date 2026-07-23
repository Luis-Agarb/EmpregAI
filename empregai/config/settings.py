"""
App configs by .env
"""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings."""

    APP_NAME: str
    APP_ENV: str
    APP_DEBUG: bool

    DB_SERVER: str
    DB_NAME: str
    DB_ODBC_DRIVER: str
    DB_TRUSTED_CONNECTION: str
    DB_ENCRYPT: str
    DB_TRUST_SERVER_CERTIFICATE: str

    LOG_LEVEL: str

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


settings = Settings()
