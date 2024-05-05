from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from django.contrib import admin
from django.urls import path, include
from core import views

schema_view = get_schema_view(
   openapi.Info(
      title="Тестовое задание для Popso",
      default_version='v1',
      description="Django Rest API приложение. Пврсинг озон.ру",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('admin_adminlte.urls')),
    path('v1/products/', views.ProductView.as_view(), name='products'),
    path('v1/products/<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),

    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
