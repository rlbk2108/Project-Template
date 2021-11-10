from django.db import models
from django.contrib.auth.models import User


PRICE = (
    ('euro', '€'),
    ('dollar', '$'),
    ('som', 'C')
)

class Photo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField('Заголовок', max_length=100)
    image = models.ImageField('Картинка', upload_to='media/')
    description = models.TextField('Описание')
    price = models.IntegerField('Цена', default=0)
    currency = models.CharField('Валюта', default='som', max_length = 200, choices=PRICE)
    date_pub = models.DateTimeField(auto_now_add=True)
    


    def __str__(self):
        return self.title