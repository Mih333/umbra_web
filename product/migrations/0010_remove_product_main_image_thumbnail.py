# Generated by Django 3.2.12 on 2022-04-01 09:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_auto_20220401_1232'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='main_image_thumbnail',
        ),
    ]
