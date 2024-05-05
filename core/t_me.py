from dotenv import load_dotenv
import os
import telegram
import requests

load_dotenv(dotenv_path='test_project/.env')
token = os.getenv('T_TOKEN')
chat_id = os.getenv('CHAT_ID')
bot = telegram.Bot(token)

def send_notification_to_telegram(products_count):
    # https://stackoverflow.com/questions/29003305/sending-telegram-message-from-python
    message = f'Задача на парсинг товаров с сайта Ozon завершена.\nСохранено: товаров - {products_count}.'
    url = 'https://api.telegram.org/bot' + token + '/sendMessage?chat_id=' + chat_id + '&parse_mode=Markdown&text=' + message
    response = requests.get(url)
    return response.json()
