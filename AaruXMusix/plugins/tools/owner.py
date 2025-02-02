from pyrogram import Client, filters
from AaruXMusix import app

from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


app.on_message(filters.command("owner") & filters.group)


async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://graph.org/file/8f3b69f3991bfb6a3eff0-9c6b31e7aa48206b18.jpg",
        caption=f"""🥀 𝐂𝐥𝐢𝐜𝐤 𝐇𝐞𝐫𝐞 𝐅𝐨𝐫 𝐂𝐨𝐧𝐭𝐚𝐜𝐭 𝐎𝐰𝐧𝐞𝐫 🥀""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Jᴀʏ sʜʀᴇᴇ ʀᴀᴍ  🚩", url=f"https://t.me/Shivang_mishra_op"
                    )],
            ]
        ),
    )


@app.on_message(filters.command("owner") & filters.group)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://graph.org/file/8f3b69f3991bfb6a3eff0-9c6b31e7aa48206b18.jpg",
        caption=f"""🥀 𝐂𝐥𝐢𝐜𝐤 𝐇𝐞𝐫𝐞 𝐅𝐨𝐫 𝐂𝐨𝐧𝐭𝐚𝐜𝐭 𝐎𝐰𝐧𝐞𝐫 🥀""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Jᴀʏ sʜʀᴇᴇ ʀᴀᴍ  🚩", url=f"https://t.me/Shivang_mishra_op"
                    )],
            ]
        ),
    )


@app.on_message(filters.command("owner") & filters.private)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://graph.org/file/8f3b69f3991bfb6a3eff0-9c6b31e7aa48206b18.jpg",
        caption=f"""🥀 𝐂𝐥𝐢𝐜𝐤 𝐇𝐞𝐫𝐞 𝐅𝐨𝐫 𝐂𝐨𝐧𝐭𝐚𝐜𝐭 𝐎𝐰𝐧𝐞𝐫 🥀""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Jᴀʏ sʜʀᴇᴇ ʀᴀᴍ  🚩", url=f"https://t.me/Shivang_mishra_op"
                    )],
            ]
        ),
    )
