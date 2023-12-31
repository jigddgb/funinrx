from pyrogram.types import InlineKeyboardButton


class Data:
    generate_single_button = [InlineKeyboardButton("✘ ɢᴇɴᴇʀᴀᴛᴇ sᴇssɪᴏɴ ✘", callback_data="generate")]

    generate_button = [generate_single_button]

    buttons = [
        generate_single_button,
        [InlineKeyboardButton("🌃 Bᴏᴛʜᴜʙ_xD 🌃", url="https://t.me/Bothub_XD"),
         InlineKeyboardButton("↳ ᴅᴇᴠᴇʟᴏᴩᴇʀ ↵", url="https://t.me/NotSuppie"),
        ],
    ]

    START = """
Hᴇʏ {},

Tʜɪs ɪs {},
Aɴ ᴏᴩᴇɴ sᴏᴜʀᴄᴇᴅ sᴛʀɪɴɢ sᴇssɪᴏɴ ɢᴇɴᴇʀᴀᴛᴏʀ ʙᴏᴛ, ᴡʀɪᴛᴛᴇɴ ɪɴ ᴩʏᴛʜᴏɴ ᴡɪᴛʜ ᴛʜᴇ ʜᴇʟᴩ ᴏғ ᴩʏʀᴏɢʀᴀᴍ.

Sᴏᴜʀᴄᴇ : [ɢɪᴛʜᴜʙ](https://t.me//Bothub_XD)
ᴅᴇᴠᴇʟᴏᴘᴇʀ : [ꜱᴜᴘᴘɪᴇ](https://t.me/NotSuppie) !
    """
