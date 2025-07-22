"""Configuration loader for HRANITEL bot."""
from dataclasses import dataclass
import os
from dotenv import load_dotenv

load_dotenv()

@dataclass
class Settings:
    """Holds configuration values loaded from environment variables."""
    bot_token: str = os.getenv("BOT_TOKEN", "")
    db_path: str = os.getenv("DB_PATH", "storage/hranitel.db")
    openai_api_key: str = os.getenv("OPENAI_API_KEY", "")

settings = Settings()

ASCII_LOGO = r"""
  _   _ _____    _   _ _____ _______ _____ _     
 | | | |  __ \  | | | |_   _|__   __|_   _| |    
 | |_| | |  | | | | | | | |    | |    | | | |    
 |  _  | |  | | | | | | | |    | |    | | | |    
 | | | | |__| | | |_| |_| |_   | |   _| |_| |____
 |_| |_|_____/   \___/|_____|  |_|  |_____|______|
"""
