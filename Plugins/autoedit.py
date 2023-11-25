import re
import logging
from pyrogram import filters, enums
from bot import AutoCaptionBot
from config import Config

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# Load configuration values
user_caption_position = Config.CAPTION_POSITION
caption_position = user_caption_position.lower()
caption_text = Config.CAPTION_TEXT
allowed_channels = Config.ALLOWED_CHANNELS
words_to_remove = Config.WORDS_TO_REMOVE
regex_patterns = Config.REGEX_PATTERNS
website_prefix = Config.WEBSITE_PREFIX
yts_website_replace = Config.YTS_WEBSITE_REPLACE

def process_caption(text, words_to_remove, regex_patterns):
    """
    Process the caption or text by removing specified words and applying regex patterns.

    Args:
        text (str): The input text.
        words_to_remove (list): List of words to be removed.
        regex_patterns (list): List of regex patterns to be applied.

    Returns:
        str: The processed text.
    """
    if words_to_remove:
        # Remove words without regex
        for word in words_to_remove:
            text = text.replace(word, "")
            text = text.strip("\n")  # remove the next line

    if regex_patterns:
        # Remove words using regex patterns
        for pattern in regex_patterns:
            text = re.sub(pattern, "", text)
            text = text.strip("\n")  # remove the next line
    
    # Remove website prefixes from caption
    if website_prefix == "REMOVE":
        # Capture everything until the first occurrence of "- " before the file extension
        text = re.sub(r'(.*?)- (.*)\.(mkv|mp4|avi)', r'\2.\3', text, flags=re.IGNORECASE)
    # Remove website prefix and add it as postfix
    elif website_prefix == "POSTFIX":
        # Capture the middle section of the link and add it before the file extension
        text = re.sub(r'www\.(.*?)\..*?( - |\.)(.*?)(\.mkv|\.mp4|\.avi)', r'\3 - \1\4', text, flags=re.IGNORECASE)
    
    if yts_website_replace:
        text = re.sub(r'\[YTS\.\w+\]', 'YTS', text, re.IGNORECASE)

    # Ensure the modified text is not empty
    if text.strip():
        text = f"**{text}**"

    return text

# Define filters for messages
f = filters.channel & (filters.document | filters.video | filters.audio | filters.text | filters.photo)

@AutoCaptionBot.on_message(f, group=-1)
@AutoCaptionBot.on_edited_message(f, group=-1)
async def editing(bot, message):
    try:
        # Identify the media type in the message
        media = message.document or message.video or message.audio or message.photo or message.text
        caption_text = f"**{Config.CAPTION_TEXT}**"  # made added caption bold
    except:
        caption_text = ""
        pass

    # Check if the current channel is in the list of allowed channels
    if allowed_channels and message.chat.id not in allowed_channels:
        logger.info("Message from a non-allowed channel. Ignoring.")
        return

    # Process the caption or text
    if media:
        if message.caption:
            file_caption = process_caption(message.caption, words_to_remove, regex_patterns)
        elif message.text:
            message_text = process_caption(message.text, words_to_remove, regex_patterns)
        else:
            fname = media.file_name
            filename = fname.replace("_", " ").replace("@", "")
            file_caption = f"`{filename}`"

    try:
        # Edit the caption based on the configured position
        if caption_position == "top":
            final_caption = ""
            if message.caption:
                final_caption = caption_text + "\n\n" + file_caption 
            elif message.text:
                final_caption = caption_text + "\n\n" + message_text 

            # Edit the message caption if it's not empty
            if final_caption.strip():
                try:
                    await bot.edit_message_caption(
                        chat_id=message.chat.id,
                        message_id=message.id,
                        caption=final_caption,
                        parse_mode=enums.ParseMode.MARKDOWN,
                    )
                except Exception as e:
                    logger.error(f"Error editing caption: {e}")

        elif caption_position == "bottom":
            final_caption = ""
            if message.caption:
                final_caption = file_caption + "\n\n" + caption_text
            elif message.text:
                final_caption = message_text + "\n\n" + caption_text

            # Edit the message caption if it's not empty
            if final_caption.strip():
                try:
                    await bot.edit_message_caption(
                        chat_id=message.chat.id,
                        message_id=message.id,
                        caption=final_caption,
                        parse_mode=enums.ParseMode.MARKDOWN,
                    )
                except Exception as e:
                    logger.error(f"Error editing caption: {e}")

        elif caption_position == "nil":
            # Edit the message caption with only the configured caption text
            try:
                await bot.edit_message_caption(
                    chat_id=message.chat.id,
                    message_id=message.id,
                    caption=caption_text,
                    parse_mode=enums.ParseMode.MARKDOWN,
                )
            except Exception as e:
                logger.error(f"Error editing caption: {e}")
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")
