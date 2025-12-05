import os

# The tokens are hardcoded in the prompt, but for security and best practice,
# we will read them from environment variables.
# The hardcoded values from the prompt are used as fallbacks for development/testing,
# but the user must set them as environment variables for deployment.

TELEGRAM_TOKEN = os.getenv(
    "TELEGRAM_TOKEN",
    "8420665033:AAHJyq728LxHiJLC061EuwOw8blnwUMMNNc" # Dummy token from prompt
)
OPENAI_API_KEY = os.getenv(
    "OPENAI_API_KEY",
    "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" # Dummy key from prompt
)
# Render requires a PORT environment variable for web service
PORT = os.getenv("PORT", 8080)

# Project specific constants
PRODUCT_BOT_USERNAME = "@Digita1_Psychology_Bot"
LANDING_PAGE_URL = "https://t.me/Digita1_Psychology_Bot"
PROJECT_NAME = "Нейропсихолог"
