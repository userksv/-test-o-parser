from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=128)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    description = models.CharField(max_length=256)
    image_url = models.CharField(max_length=128)
    discount = models.CharField(max_length=64, null=True, blank=True)

    def __str__(self) -> str:
        return f'{self.name}'