# Generated by Django 2.2.6 on 2020-09-09 23:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_auto_20200910_0014'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='sku',
        ),
    ]
