import asyncio
from celery import shared_task
from core.get_data import get_data_from_website
from core.serializers import ProductSerializer
from core.t_me import send_notification_to_telegram

def write_last_added_items(last_added: list):
    open('last_added.txt', 'w').close()
    with open('last_added.txt', 'w') as file:
        for i, item in enumerate(last_added, 1):
            file.write(f'{i}. {item["name"]} - {item["url"]}\n')

@shared_task
def start_parsing_task(products_count):
    data = get_data_from_website(products_count)
    i = 0
    for item in data:
        serializer = ProductSerializer(data=item)
        if serializer.is_valid():
            if i >= products_count:
                break
            serializer.save()
            i += 1

    write_last_added_items(data)
    send_notification_to_telegram(i)