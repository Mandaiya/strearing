from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

from config import OWNER_ID

# Renaming the filter function to avoid conflict with built-in names
def command_filter(cmd: str):
    return filters.private & filters.incoming & filters.command(cmd)

@Client.on_message(command_filter("start"))
async def start(bot: Client, msg: Message):
    me = (await bot.get_me()).mention  # Changed variable name to avoid shadowing built-in function name 'me'
    await msg.reply_text(
        text=f"""ʜᴇʏ {msg.from_user.mention},

ᴡᴇʟᴄᴏᴍᴇ ! {me},
╰★ I am an Stringene Robot - use me to generate the strings for your Bots ★╯
ᴅᴏɴ'ᴛ ᴡᴀꜱᴛᴇ ʏᴏᴜʀ ᴠᴀʟᴜᴀʙʟᴇ ᴛɪᴍᴇ ᴀɴᴅ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ " 𝐒𝐭𝐫𝐢𝐧𝐠𝐞𝐧𝐞 "!!

𝘾𝙧𝙚𝙖𝙩𝙤𝙧: [┣▇-𝚂𝚅𝙳 ▇-->](https://t.me/Soupboy_single) !""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="|-〄 STRINGENE 〄-|", callback_data="generate")
                ],
                [
                    InlineKeyboardButton(-🔫 Gamers Society -🔫", url="https://t.me/smarhkarts_gAme"),
                    InlineKeyboardButton("|-⦾ Network ⦾-|", url="https://t.me/we_are_universee")
                ]
            ]
        ),
        disable_web_page_preview=True,
    )
