<h1 align='center'>🖊️ TG AutoCaption Bot </h1>

<h4 align='center'>
    Telegram Bot for Auto Captioning Files & Videos with Custom Text<br><br>
    <i>(Exclusive to public or private Telegram channels)</i> 
</h4><br>

## Overview

TG AutoCaption Bot is a Telegram bot designed to automatically caption files and videos in your channels. With customizable settings, it can add and remove certain text to the caption.

## Configuration

Edit the `config.py` file to customize the bot behavior according to your preferences. Below are some key configuration options:

- `CAPTION_TEXT`: Caption to be added below the file (Markdown supported).
- `CAPTION_POSITION`: Position of the caption relative to the file name (TOP or BOTTOM or NIL).
- `ADMIN_USERNAME`: Username to display in bot PM (without "@").
- `WORDS_TO_REMOVE`: List of words to remove from existing captions.
- `REGEX_PATTERNS`: List of regex patterns to remove from existing captions.
- `ALLOWED_CHANNELS`: List of channel IDs to allow the bot. Leave empty to allow in all channels.
- `WEBSITE_PREFIX`: Decide what to do with the caption text if it starts with a website (REMOVE or POSTFIX or NIL).
- `YTS_WEBSITE_REPLACE`: Replace YIFY website credits with YTS (True or False).

## Deployment

### Local Deployment

1. Download this repository.
2. Install required packages using 
```
pip3 install -r requirements.txt
```
3. Edit the `config.py` file to configure variables.
4. Run the bot using 
```
python3 bot.py
```

## Commands

- `/start`: Start the bot.
- `/help`: Get assistance on using the bot.
- `/about`: Learn more about the bot.
- `/source`: View the source code.

## Credits

This repository is a modification of [Caption Bot](https://github.com/avipatilpro/Caption-Bot) by [avipatilpro](https://github.com/avipatilpro). Special thanks for the original implementation.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
