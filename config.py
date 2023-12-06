import os


class Config(object):
    # env vars
    BOT_TOKEN = "1234567890:ABCDEFGHIJKLMNOPQRSTUVWXYZ"  # string
    API_ID = 1234567  # int
    API_HASH = "123abc456def789ghi012jklmn"  # string
    
    # db vars
    # keep empty if don't want to add any extra caption
    CAPTION_TEXT = "Added this caption"  
    # BOTTOM or TOP or NIL
    CAPTION_POSITION = "BOTTOM"  
    ADMIN_USERNAME = "username"  # without "@". 

    # a list of strings of words to remove from the existing caption
    WORDS_TO_REMOVE = []  
    # a list of regex pattern strings to remove from the existing caption. 
    # For eg. r".*Join.*" will remove the entire line having word Join
    REGEX_PATTERNS = []  

    # keep empty to allow in all channels. Can add multiple channels separated by a comma.
    # Don't forget -100 before the channel ID
    ALLOWED_CHANNELS = [-100123456789]

    # REMOVE or POSTFIX or NIL. Useful for tamilblasters, tamilmv and other webites
    WEBSITE_PREFIX = "POSTFIX"  

    # True or False. Replaces YIFY website with YTS
    YTS_WEBSITE_REPLACE = True 

    # Dictionary of words to replace
    REPLACE_DICTIONARY = {}
