from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "InvestAdvisor"
    DATABASE_URL: str = "postgresql+asyncpg://user:pass@localhost/dbname"
    SECRET_KEY: str = "super-secret-jwt-key-2026"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 1440

    class Config:
        env_file = ".env"

settings = Settings()
