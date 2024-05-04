from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from core.fetch_data import get_data
from core.serializers import ProductSerializer

class ProductView(APIView):
    
    def post(self, request):
        products_count = request.data['products_count'] if request.data else 10
        data = get_data(int(products_count))
        for item in data:
            serializer = ProductSerializer(data=item)
            if serializer.is_valid():
                serializer.save()

        return Response({'response': 'Response from POST'})
    
    def get(self, request, id=None):
        # if id get product detail from db and return in response
        # get all records from db 
        return Response({'response': 'Test response'})
