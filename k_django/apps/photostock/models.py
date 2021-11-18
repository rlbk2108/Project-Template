from django.db import models
from django.contrib.auth.models import User


TYPE_OF_PRODUCT = (
    ('euro', '€'),
    ('dollar', '$'),
    ('som', 'C')
)

class Warehouse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
<<<<<<< HEAD
    email = models.EmailField('Почта', max_length=100, default=user)
    title = models.CharField('Заголовок', max_length=100)
    image = models.ImageField('Картинка', upload_to='media/')
    description = models.TextField('Описание')
    price = models.IntegerField('Цена', default=0)
    currency = models.CharField('Валюта', default='som', max_length = 200, choices=PRICE)
=======
    # storage = models.CharField('Склад', default='som', max_length = 200, choices=TYPE_OF_PRODUCT)
    product_name = models.CharField('Название товара', max_length=100)
    product_number = models.IntegerField('Количество товара', default=0)
>>>>>>> 017fc8feb087caab074262456c3bca2009da94bd
    date_pub = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.product_name