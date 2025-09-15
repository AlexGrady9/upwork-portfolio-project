"""Application settings and configuration."""

import os
from functools import lru_cache
from typing import Optional


class Settings:
    def __init__(self):
        self.DEBUG = True
        self.LOG_LEVEL = "INFO"
        self.SECRET_KEY = "dev-secret-key-change-in-production"
        self.DATABASE_URL = "sqlite:///./app.db"
        self.API_V1_PREFIX = "/api/v1"


@lru_cache()
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
