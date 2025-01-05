from telethon import TelegramClient, events
from dotenv import load_dotenv
import os

# Load API dari .env
load_dotenv("bot.env")

print("File .env berhasil dimuat:", os.path.exists('bot.env'))

# Ambil nilai dari .env
api_id = os.getenv("API_ID")
api_hash = os.getenv("API_HASH")
bot_token = os.getenv("BOT_TOKEN")

# Periksa jika api_id, api_hash, atau bot_token kosong
if not api_id or not api_hash:
    raise ValueError("API ID atau API Hash tidak boleh kosong!")
if not bot_token:
    raise ValueError("Bot Token tidak boleh kosong!")

print(f"API ID: {api_id}")
print(f"API Hash: {api_hash}")
print(f"Bot Token: {bot_token}")

client = TelegramClient('bot_session', api_id, api_hash).start(bot_token=bot_token)

source_channel = '@sol_trend'
destination_channel = '@signprtmnnd'

@client.on(events.NewMessage(chats=source_channel))
async def handler(event):
    if event.message.media:
        await client.send_message(destination_channel, event.message, file=event.message.media)
    else:
        await client.send_message(destination_channel, event.message)

print("Bot is running...")
client.run_until_disconnected()
