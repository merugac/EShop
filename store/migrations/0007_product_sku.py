# Generated by Django 2.2.6 on 2020-09-09 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_remove_product_sku'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='sku',
            field=models.IntegerField(default=0),
        ),
    ]
