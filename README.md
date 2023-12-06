<h1 align='center'>🖊️ TG AutoCaption Bot </h1>

<h4 align='center'>
    Telegram Bot for Auto Captioning Files & Videos with Custom Text<br><br>
    <i>(Exclusive to public or private Telegram channels)</i> 
</h4><br>

## Overview

TG AutoCaption Bot is a Telegram bot designed to automatically caption files and videos in your channels. With customizable settings, it can add and remove certain text from the caption.

## Configuration

1. **Create a Bot on Telegram:**
   - Start by creating a new bot on Telegram using [@BotFather](https://t.me/BotFather).
   - After creating the bot, add it to your channel and grant it "Manage Messages" admin rights.

2. **Edit the `config.py` file:**
   - Customize the bot behavior according to your preferences by editing the `config.py` file.
   - Below are some key configuration options:

     - `CAPTION_TEXT`: Caption to be added below the file (Markdown supported).
     - `CAPTION_POSITION`: Position of the caption relative to the file name (TOP or BOTTOM or NIL).
     - `ADMIN_USERNAME`: Username to display in bot PM (without "@").
     - `WORDS_TO_REMOVE`: List of words to remove from existing captions.
     - `REGEX_PATTERNS`: List of regex patterns to remove from existing captions.
     - `ALLOWED_CHANNELS`: List of channel IDs to allow the bot. Leave empty to allow in all channels.
     - `WEBSITE_PREFIX`: Decide what to do with the caption text if it starts with a website (REMOVE or POSTFIX or NIL).
     - `YTS_WEBSITE_REPLACE`: Replace YIFY website credits with YTS (True or False).
     - `REPLACE_DICTIONARY`: Dictionary of key value pairs of original word in the caption to replace with another word.

## Deployment

### Local Deployment

1. **Download this repository:**
   - Clone or download this repository to your local machine.

2. **Install required packages:**
   - Open a terminal and run the following command:
     ```bash
     pip3 install -r requirements.txt
     ```

3. **Configure variables:**
   - Edit the `config.py` file to set up your bot according to your preferences.

4. **Run the bot:**
   - Start the bot by running the following command in your terminal:
     ```bash
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
