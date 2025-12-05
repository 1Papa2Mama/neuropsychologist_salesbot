import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message
from config import TELEGRAM_TOKEN, PORT
from .handlers.message_handler import start_command_handler, text_message_handler

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher()

# Register handlers
dp.message.register(start_command_handler, CommandStart())
dp.message.register(text_message_handler)

async def main():
    """
    Main function to start the bot.
    Uses long polling for simplicity in a non-webhook environment.
    For Render deployment, we will need to switch to webhooks.
    """
    logging.info("Starting bot...")
    # Delete webhook before starting long-polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

# --- Webhook setup for Render deployment ---
# This part is crucial for the deployment instruction.
# The user will need to run this file with a different command for webhook.

async def start_webhook():
    """
    Starts the bot using webhooks, suitable for platforms like Render.
    """
    from aiohttp import web
    from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application

    # The webhook URL will be provided by Render
    WEBHOOK_HOST = os.getenv('WEBHOOK_HOST')
    if not WEBHOOK_HOST:
        logging.error("WEBHOOK_HOST environment variable is not set. Cannot start webhook.")
        return

    WEBHOOK_PATH = f"/webhook/{TELEGRAM_TOKEN}"
    WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"

    # Set webhook
    await bot.set_webhook(WEBHOOK_URL)

    # Create aiohttp application
    app = web.Application()
    
    # Create request handler
    webhook_requests_handler = SimpleRequestHandler(
        dispatcher=dp,
        bot=bot,
    )
    
    # Register handler in application
    webhook_requests_handler.register(app, path=WEBHOOK_PATH)
    
    # Setup application
    setup_application(app, dp, bot=bot)

    # Start web server
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, host='0.0.0.0', port=PORT)
    logging.info(f"Starting web server on port {PORT}...")
    await site.start()
    
    # Keep the main task running
    while True:
        await asyncio.sleep(3600)

if __name__ == "__main__":
    import os
    # Check if WEBHOOK_HOST is set to decide between polling and webhook
    if os.getenv('WEBHOOK_HOST'):
        asyncio.run(start_webhook())
    else:
        # Fallback to long polling for local development
        asyncio.run(main())
