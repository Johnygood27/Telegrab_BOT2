# HRANITEL Telegram Bot

HRANITEL is an extensible Telegram bot built with [aiogram](https://docs.aiogram.dev/) v3.
It logs incoming messages to SQLite and lays the groundwork for future OSINT and AI-powered analysis features.

## Features
- `/start` prints an ASCII logo and welcome text
- `/help` lists available commands
- Replies to any text with a standard acknowledgement
- Stores username, user id, timestamp, and content in SQLite
- Rate limited to **1 message per 5 seconds** per user
- Error logs written to `error.log`

## Setup
1. Create a virtual environment (Python 3.11+ recommended)
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
2. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```
3. Configure environment variables
   ```bash
   cp .env.example .env
   # edit .env with your BOT_TOKEN and optional settings
   ```
4. Run the bot
   ```bash
   python main.py
   ```

The bot uses polling and creates a SQLite database at the path specified by `DB_PATH`.
