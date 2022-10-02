import asyncio

from helpers.filters import command
from config import BOT_NAME as bn, BOT_USERNAME as bu, CHANNEL_UPDATES, SUPPORT_GROUP, OWNER_USERNAME as me, START_IMG
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(command("start") & filters.private & ~filters.group & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_sticker("CAACAgIAAx0CZD3aQwACJD1jJ-k4Y3XA0H9cEU6QHfPxyNZjhwAC6BYAAv2LEEra9hZZ9LdRQCkE")
    await message.reply_photo(
        photo=f"{START_IMG}",
        caption=f"""**━━━━━━━━━━━━━━━━━━
 ʜᴀʏ {message.from_user.mention()} 🤍! 

     ᴛʜɪs ɪs [{bn}](t.me/{bu}), ᴀ sᴜᴘᴇʀ ғᴀsᴛ ᴠᴄ ᴘʟᴀʏᴇʀ ʙᴏᴛ ғᴏʀ ᴛᴇʟᴇɢʀᴀᴍ ɢʀᴏᴜᴘ ᴠᴏɪᴄᴇᴄʜᴀᴛ. Mᴀɴᴀɢᴇᴅ ʙʏ ʀ.ᴏɴᴇ ᴏᴘ..

• ᴀʟʟ ᴏғ ᴍʏ ᴄᴏᴍᴍᴀɴᴅ ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ᴡɪᴛʜ ᴍʏ ᴄᴀᴍᴍɴᴅ ʜᴀɴᴅʟᴇ : ( `/ . • $ ^ ~ + * ?` )

• ɪғ ʏᴏᴜ ʜᴀᴠᴇ ᴀɴʏ ǫᴜᴇsᴛɪᴏɴs ᴀʙᴏᴜᴛ ᴍᴇ ᴛʜᴇɴ ᴅᴍ ᴛᴏ ᴍʏ [ᴏᴡɴᴇʀ](t.me/{me}) ...
━━━━━━━━━━━━━━━━━━**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✚ ᴀᴅᴅ ᴍᴇ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ ʙᴀʙʏ", url=f"https://t.me/{bu}?startgroup=true"
                       ),
                  ],[
                    InlineKeyboardButton(
                        "📨 ᴄʜᴀɴɴᴇʟ ", url=f"https://t.me/{CHANNEL_UPDATES}"
                    ),
                    InlineKeyboardButton(
                        "📨 sᴜᴘᴘᴏʀᴛ ", url=f"https://t.me/{SUPPORT_GROUP}"
                    )
                  ],[
                    InlineKeyboardButton(
                        "👤 ᴍʏ ʙᴀʙʏ ", url=f"https://t.me/{me}"
                    ),
                    InlineKeyboardButton(
                        "👨‍💻 ᴄᴏᴅᴇ ᴏᴡɴᴇʀ ", url=f"https://t.me/R_ONE_HU"
                    ),
                  ],[
                    InlineKeyboardButton(
                        "✅ ɪɴʟɪɴᴇ ", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "💡 ғɪʟʟᴇɴɢs", url="https://t.me/FunTwenty_4"
                    )]
            ]
       ),
    )

