# Generated by Django 3.2.8 on 2021-11-04 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photostock', '0003_auto_20211019_1324'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='category',
        ),
        migrations.AddField(
            model_name='photo',
            name='price',
            field=models.CharField(choices=[('euro', '€'), ('dollar', '$'), ('som', 'C')], default=0, max_length=200, verbose_name='Цена'),
            preserve_default=False,
        ),
    ]
