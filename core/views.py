from django.http import HttpResponse, JsonResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from core.serializers import ProductSerializer
from core.models import Product
from core.tasks import start_parsing_task

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class ProductView(APIView):
    @swagger_auto_schema(
        operation_description='''POST /v1/products/ body: products_count=10 (по умолчанию 10 (если значение не было передано), максимум 50)
                        Запрос на парсинг озон и сохранение данных в БД.''',
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'products_count': openapi.Schema(type=openapi.TYPE_NUMBER, default=10),
            },
        ),
        responses={200: 'Ok', 400: 'Bad Request'}
    )
    def post(self, request):
        products_count = request.data['products_count'] if request.data else 10
        if int(products_count) > 50:
            return Response({'response': 'превышенно максимальное кол-во запрашиваемых данных!'})
        start_parsing_task.delay(int(products_count))
        return Response(status=status.HTTP_200_OK)
    
    @swagger_auto_schema(
        operation_description='''GET - /v1/products/ (Получение списка товаров)''',
        responses={200: 'Ok', 400: 'Bad Request'}
    )
    def get(self, reauest):
        try:
            products = Product.objects.distinct()
            serializer = ProductSerializer(products, many=True)
            return Response(serializer.data)
        except Product.DoesNotExist:
            return HttpResponse(status=404)


class ProductDetailView(APIView):
    def get_product(self, pk):
        try:
            return Product.objects.get(id=pk)
        except Product.DoesNotExist:
            return HttpResponse(status=404)
        
    @swagger_auto_schema(
        operation_description='''GET - /v1/products/{product_id}/ (Получение товара по айди)''',
        responses={200: 'Ok', 404: 'Not Found'},
    )
    def get(self, request, pk=None):
        if pk != None:
            product = self.get_product(pk)
            serializer = ProductSerializer(product)
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.data, safe=False)
