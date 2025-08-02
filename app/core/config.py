import os


class Settings:
    """Simple settings object that reads configuration from environment variables."""

    def __init__(self) -> None:
        self.DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./app.db")


settings = Settings()

