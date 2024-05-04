from django.http import HttpResponse, JsonResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from core.get_data import get_data_from_website
from core.serializers import ProductSerializer
from core.models import Product
from core.t_me import send_notification_to_telegram
from core.management.commands.bot import last_added_items
import asyncio


class ProductView(APIView):

    def write_last_added_items(self, last_added: list):
        open('last_added.txt', 'w').close()
        with open('last_added.txt', 'a')as file:
            for i, item in enumerate(last_added, 1):
                file.write(f'{i}. {item["name"]} - {item["url"]}\n')
                

    def post(self, request):
        products_count = request.data['products_count'] if request.data else 10
        if int(products_count) > 50:
            return Response({'response': 'превышенно максимальное кол-во запрашиваемых данных!'})
        data = get_data_from_website(int(products_count))
        self.write_last_added_items(data)
        for item in data:
            serializer = ProductSerializer(data=item)
            if serializer.is_valid():
                serializer.save()
        # message for telegram put this to celery?
        asyncio.run(send_notification_to_telegram(products_count))
        return Response(status=status.HTTP_200_OK)
    
    def get_product(self, pk):
        try:
            return Product.objects.get(id=pk)
        except Product.DoesNotExist:
            return HttpResponse(status=404)
        
    def get_all_products(self):
        try:
            return Product.objects.distinct()
        except Product.DoesNotExist:
            return HttpResponse(status=404)

    def get(self, request, pk=None):
        # if pk get product detail from db and return in response
        if pk != None:
            product = self.get_product(pk)
            serializer = ProductSerializer(product)
            return JsonResponse(serializer.data)
        # get all records from db 
        products = self.get_all_products()
        serializer = ProductSerializer(products, many=True)

        return JsonResponse(serializer.data, safe=False)
