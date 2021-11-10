# Generated by Django 3.2.8 on 2021-11-04 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photostock', '0004_auto_20211104_2045'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='currency',
            field=models.CharField(choices=[('euro', '€'), ('dollar', '$'), ('som', 'C')], default='som', max_length=200, verbose_name='Валюта'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='price',
            field=models.IntegerField(default=0, verbose_name='Цена'),
        ),
    ]