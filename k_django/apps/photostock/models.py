from django.db import models
from django.contrib.auth.models import User


TYPE_OF_PRODUCT = (
    ('euro', '€'),
    ('dollar', '$'),
    ('som', 'C')
)

class Warehouse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # storage = models.CharField('Склад', default='som', max_length = 200, choices=TYPE_OF_PRODUCT)
    product_name = models.CharField('Название товара', max_length=100)
    product_number = models.IntegerField('Количество товара', default=0)
    date_pub = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.product_name