import asyncio
from django.http import HttpResponse, JsonResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from core.serializers import ProductSerializer
from core.models import Product
from core.tasks import start_parsing_task
from time import sleep


class ProductView(APIView):
             
    def post(self, request):
        products_count = request.data['products_count'] if request.data else 10
        if int(products_count) > 50:
            return Response({'response': 'превышенно максимальное кол-во запрашиваемых данных!'})
        start_parsing_task.delay(int(products_count))
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
        if pk != None:
            product = self.get_product(pk)
            serializer = ProductSerializer(product)
            return JsonResponse(serializer.data)
        # get all records from db 
        products = self.get_all_products()
        serializer = ProductSerializer(products, many=True)

        return JsonResponse(serializer.data, safe=False)
