from telethon import TelegramClient, events
import os
import asyncio
from dotenv import load_dotenv
import requests

load_dotenv()

api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
bot_token = os.getenv("BOT_TOKEN")
chat_id = int(os.getenv("DESTINATION_CHAT_ID"))
thread_id = int(os.getenv("DESTINATION_THREAD_ID"))

source_chats = [
    "https://t.me/oCkPs7QOIHoxNGIy",
    "https://t.me/+Hg0Vi3K2gG05N2Qy",
    "https://t.me/tigrqwe",
    "https://t.me/kastingsalmaty",
    "https://t.me/cinema_association"
]

client = TelegramClient("mirror_session", api_id, api_hash)

@client.on(events.NewMessage(chats=source_chats))
async def handler(event):
    try:
        msg = event.message.message
        if msg:
            send_url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
            payload = {
                "chat_id": chat_id,
                "message_thread_id": thread_id,
                "text": msg
            }
            requests.post(send_url, json=payload)
            print(f"✅ Отправлено в тему: {msg[:50]}...")
    except Exception as e:
        print(f"⚠️ Ошибка при отправке: {e}")

async def main():
    print("♻️ Зеркало запущено.")
    await client.run_until_disconnected()

client.start()
client.loop.run_until_complete(main())
