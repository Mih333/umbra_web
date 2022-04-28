# Generated by Django 3.2.12 on 2022-03-30 08:36

from django.db import migrations, models
import django.db.models.deletion
import djangocms_text_ckeditor.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cms', '0022_auto_20180620_1551'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='product_product', serialize=False, to='cms.cmsplugin')),
                ('title', models.CharField(help_text='Product name', max_length=350, null=True)),
                ('content', djangocms_text_ckeditor.fields.HTMLField(blank=True, help_text='Product description', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
