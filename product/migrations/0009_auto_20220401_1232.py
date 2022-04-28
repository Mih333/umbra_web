# Generated by Django 3.2.12 on 2022-04-01 09:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0014_folder_permission_choices'),
        migrations.swappable_dependency(settings.FILER_IMAGE_MODEL),
        ('product', '0008_alter_product_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='main_image_thumbnail',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product_thumbnail', to='filer.thumbnailoption', verbose_name='main image thumbnail'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product_image', to=settings.FILER_IMAGE_MODEL, verbose_name='product image'),
        ),
    ]