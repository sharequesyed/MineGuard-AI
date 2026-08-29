import os

class Settings:
    PROJECT_NAME: str = "MineGuard AI API"
    VERSION: str = "1.0.0"
    API_PREFIX: str = "/api"
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./mineguard.db")
    SECRET_KEY: str = os.getenv("SECRET_KEY", "sih2026-mineguard-secret-key-minenova6")
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "development")

settings = Settings()
