import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)

logging.getLogger("pyrogram").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)

from config import Config
from pyrogram import Client

class AutoCaptionBot(Client):
    def __init__(self):
        super().__init__(
            name="Captioner",
            bot_token=Config.BOT_TOKEN,
            api_id=Config.API_ID,
            api_hash=Config.API_HASH,
            workers=20,
            plugins=dict(root="Plugins"),
        )
        
        # Enable additional logging for Pyrogram
        self.log_verbosity = logging.INFO

    def run(self):
        try:
            logger.info("Bot is starting...")
            super().run()
            logger.info("Bot is up and running.")
        except Exception as e:
            logger.error(f"An error occurred during bot execution: {e}")
        finally:
            logger.info("Bot is shutting down.")

if __name__ == "__main__":
    AutoCaptionBot().run()
