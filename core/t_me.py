from dotenv import load_dotenv
import os
import telegram

load_dotenv(dotenv_path='test_project/.env')
token = os.getenv('T_TOKEN')
chat_id = os.getenv('CHAT_ID')
bot = telegram.Bot(token)

async def send_notification_to_telegram(products_count):
    message = f'Задача на парсинг товаров с сайта Ozon завершена.\nСохранено: {products_count} товаров.'
    await bot.send_message(chat_id=chat_id, text=message)

