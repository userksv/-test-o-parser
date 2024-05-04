from django.http import HttpResponse, JsonResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from core.get_data import get_data_from_website
from core.serializers import ProductSerializer
from core.models import Product

class ProductView(APIView):
    
    def post(self, request):
        products_count = request.data['products_count'] if request.data else 10
        if int(products_count) > 50:
            return Response({'response': 'превышенно максимальное кол-во запрашиваемых данных!'})
        data = get_data_from_website(int(products_count))
        for item in data:
            serializer = ProductSerializer(data=item)
            if serializer.is_valid():
                serializer.save()
        # send notification to telegram
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
