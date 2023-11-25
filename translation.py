class Translation(object):
    START_TEXT = """
Hi __{}__ , 

__I Am Auto Caption Bot__

__I can automatically remove or add caption to the files posted in the channels.__

**Maintained by __@{}__**
"""

    HELP_TEXT = """
<u><b>Help</b></u> 

<i>Add me as an Admin in your channel with edit permission</i>

<i>Add your caption in .env/config var</i>
   
<i>[Supports Markdown]</i>

<i>Forward your files in your channel and I will edit it</i>

<b>My Source Code : /source</b>

"""

    ABOUT_TEXT = """
**About Me**

__My Name: AutoCaptionBot
Language : Python 
Framework : Pyrogram
Server : Heroku
Version : 2.0.1
Creator :  @shubham_indalkar__
 
"""

    MARKDOWN_TEXT = """
<u><b>About Markdown</b></u>

<b>Bold text</b>
<code>**Telegram**</code>

<b>Italic text</b>
<code>__Telegram__</code> 

<b>Spoiler text</b>
<code>||Telegram||</code>

<b>Code text</b>
<code>```Telegram```</code>   

<b>Hyperlink text</b>
<code>[hyperlink_text](https://telegram.org/)</code>

"""

    # Bot status display

    STATUS_DATA = """
<u><b>Bot Status</b></u>

<b>Current Caption :</b> 
{}

<b>Current Position :</b> <i>{}</i>

"""

    SOURCE_TEXT = """

<b> I Am Available Open Source on Github 
      Click Below Link And Deploy Me Now </b>

<i>DEPLOY</i> : <b><a href="https://heroku.com/deploy?template=https://github.com/avipatilpro/Caption-Bot">On Heroku</a></b>    

<i>SOURCE</i> : <b><a href="https://github.com/avipatilpro/Caption-Bot">Caption Bot</a></b>  
"""

    # Removed text display

    REMOVED_TEXT = """
<u><b>Bot Status</b></u>

<b>Removed text :</b> 
<i>{}</i>

"""
