import os

# --- Tokens (must be provided in Render environment variables) ---
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# --- Render-specific ---
PORT = os.getenv("PORT", 8080)

# --- Project constants ---
PRODUCT_BOT_USERNAME = "@Digita1_Psychology_Bot"
LANDING_PAGE_URL = "https://digipsyland-mrufvje5.manus.space"
PROJECT_NAME = "Нейропсихолог"
