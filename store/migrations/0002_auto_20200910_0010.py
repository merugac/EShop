# Generated by Django 2.2.6 on 2020-09-09 23:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='sku',
            new_name='prod_id',
        ),
    ]
