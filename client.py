from telethon import TelegramClient
import os

# دریافت اطلاعات از فایل .env
API_ID = os.getenv("TELEGRAM_API_ID")
API_HASH = os.getenv("TELEGRAM_API_HASH")

def get_client():
    """ایجاد و بازگرداندن کلاینت تلگرام"""
    # سشن با نام 'aegis_session' ذخیره می‌شود
    client = TelegramClient('aegis_session', API_ID, API_HASH)
    return client
