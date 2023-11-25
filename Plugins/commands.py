import logging
from pyrogram import filters, enums
from bot import AutoCaptionBot
from config import Config
from translation import Translation
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# variable to keep track of the original command
original_command = None

# all buttons

# start buttons
start_button = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("🖋 Current Caption", callback_data="status_data"),
            InlineKeyboardButton("🗑️ Removed Text", callback_data="removed_text_data"),
        ],
        [
            InlineKeyboardButton("💡 Help", callback_data="help_data"),
            InlineKeyboardButton("ℹ️ About", callback_data="about_data"),
        ],
        [InlineKeyboardButton("❌ Close", callback_data="close_data")],
    ]
)

# help buttons
help_button = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton("ABOUT MARKDOWN", callback_data="markdown_data")],
        [
            # InlineKeyboardButton("⏪ BACK", callback_data="back_data"),
            InlineKeyboardButton("❌ CLOSE", callback_data="close_data"),
        ],
    ]
)

# about buttons
about_button = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton("💡 Help", callback_data="help_data")],
        [
            # InlineKeyboardButton("⏪ BACK", callback_data="back_data"),
            InlineKeyboardButton("❌ CLOSE", callback_data="close_data"),
        ],
    ]
)

# source Buttons
source_button = InlineKeyboardMarkup(
    [
        [
            # InlineKeyboardButton("⏪ Back", callback_data="back_data"),
            InlineKeyboardButton("❌ Close", callback_data="close_data"),
        ]
    ]
)

# removed text buttons
removed_text_button = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton("⏪ BACK", callback_data="back_data"),
         InlineKeyboardButton("❌ CLOSE", callback_data="close_data")],
    ]
)

@AutoCaptionBot.on_message(filters.command("start") & filters.private)
async def start(bot, cmd):
    global original_command
    original_command = "start"

    await bot.send_message(
        chat_id=cmd.chat.id,
        text=Translation.START_TEXT.format(
            cmd.from_user.first_name, Config.ADMIN_USERNAME
        ),
        reply_to_message_id=cmd.id,
        parse_mode=enums.ParseMode.MARKDOWN,
        disable_web_page_preview=True,
        reply_markup=start_button,
    )

@AutoCaptionBot.on_message(filters.command("help") & filters.private)
async def help(bot, cmd):
    global original_command
    original_command = "help"

    await bot.send_message(
        chat_id=cmd.chat.id,
        text=Translation.HELP_TEXT,
        reply_to_message_id=cmd.id,
        parse_mode=enums.ParseMode.HTML,
        disable_web_page_preview=True,
        reply_markup=help_button,
    )

@AutoCaptionBot.on_message(filters.command("about") & filters.private)
async def about(bot, cmd):
    global original_command
    original_command = "about"

    await bot.send_message(
        chat_id=cmd.chat.id,
        text=Translation.ABOUT_TEXT,
        reply_to_message_id=cmd.id,
        parse_mode=enums.ParseMode.MARKDOWN,
        disable_web_page_preview=True,
        reply_markup=about_button,
    )

@AutoCaptionBot.on_message(filters.command("source") & filters.private)
async def source(bot, cmd):
    await bot.send_message(
        chat_id=cmd.chat.id,
        text=Translation.SOURCE_TEXT,
        reply_to_message_id=cmd.id,
        parse_mode=enums.ParseMode.HTML,
        disable_web_page_preview=True,
        reply_markup=source_button,
    )

@AutoCaptionBot.on_callback_query()
async def button(bot, cmd: CallbackQuery):
    global original_command
    cb_data = cmd.data
    
    if "about_data" in cb_data:
        await cmd.message.edit(
            text=Translation.ABOUT_TEXT,
            parse_mode=enums.ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("⏪ BACK", callback_data="back_data"),
                        InlineKeyboardButton("❌ CLOSE", callback_data="close_data"),
                    ]
                ]
            ),
        )
    elif "source_data" in cb_data:
        await cmd.message.edit(
            text=Translation.SOURCE_TEXT,
            parse_mode=enums.ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        # InlineKeyboardButton("⏪ BACK", callback_data="back_data"),
                        InlineKeyboardButton("❌ CLOSE", callback_data="close_data"),
                    ]
                ]
            ),
        )
    elif "help_data" in cb_data:
        if original_command in ["start", "about"]:
            back_button = [
                            InlineKeyboardButton("⏪ BACK", callback_data="back_data"),
                            InlineKeyboardButton("❌ CLOSE", callback_data="close_data"),
                        ]  
        else:
            back_button = [
                            InlineKeyboardButton("❌ CLOSE", callback_data="close_data"),
                        ]  

        await cmd.message.edit(
            text=Translation.HELP_TEXT,
            parse_mode=enums.ParseMode.HTML,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("ABOUT MARKDOWN", callback_data="markdown_data")
                    ],
                    back_button,
                    
                ]
            ),
        )
    elif "back_data" in cb_data:
        keyboard_markup = about_button if original_command == "about" else start_button
        
        await cmd.message.edit(
            text=Translation.START_TEXT.format(
                cmd.from_user.first_name, Config.ADMIN_USERNAME
            ),
            parse_mode=enums.ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=keyboard_markup,
        )
    elif "close_data" in cb_data:
        await cmd.message.delete()
        await cmd.message.reply_to_message.delete()
    elif "markdown_data" in cb_data:
        await cmd.message.edit(
            text=Translation.MARKDOWN_TEXT,
            parse_mode=enums.ParseMode.HTML,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("⏪ BACK", callback_data="help_data"),
                        InlineKeyboardButton("❌ CLOSE", callback_data="close_data"),
                    ]
                ]
            ),
        )
    elif "status_data" in cb_data:
        await cmd.message.edit(
            text=Translation.STATUS_DATA.format(
                Config.CAPTION_TEXT, Config.CAPTION_POSITION
            ),
            parse_mode=enums.ParseMode.HTML,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("⏪ BACK", callback_data="back_data"),
                        InlineKeyboardButton("❌ CLOSE", callback_data="close_data"),
                    ]
                ]
            ),
        )
    elif "removed_text_data" in cb_data:
        removed_text = "\n".join(Config.WORDS_TO_REMOVE) + "\n"+ "\n".join(Config.REGEX_PATTERNS)
        await cmd.message.edit(
            text=Translation.REMOVED_TEXT.format(removed_text),
            parse_mode=enums.ParseMode.HTML,
            disable_web_page_preview=True,
            reply_markup=removed_text_button,
        )
 