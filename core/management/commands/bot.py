from django.core.management.base import BaseCommand
import asyncio
from dotenv import load_dotenv
import os
import telegram
from telegram import Update
from telegram.ext import CommandHandler, ContextTypes, Application

class Command(BaseCommand):
    help = 'Telegram bot'

    def handle(self, *args, **options) -> str | None:
        asyncio.run(main())

load_dotenv(dotenv_path='test_project/.env')
token = os.getenv('T_TOKEN')
chat_id = os.getenv('CHAT_ID')
bot = telegram.Bot(token)

def read_file():
    filename = 'last_added.txt'
    data = []
    with open(filename, 'r')as file:
        for line in file:
            line.replace('\n', ' ').strip()
            data.append(line)
    return data

def last_added_items(last_added: list):
    message = ''
    for line in last_added:
        message += f'{line}'
    return message


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Welcome')

async def handle_products(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # get last parsing with products 
    await update.message.reply_text(last_added_items(read_file()))


def main():
    app = Application.builder().token(token).build()

    app.add_handler(CommandHandler('start', start))
    app.add_handler(CommandHandler('products', handle_products))

    app.run_polling(poll_interval=3)
