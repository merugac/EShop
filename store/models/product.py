from django.db import models
from .category import Category
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    sku = models.IntegerField(null=True)
    name = models.CharField(blank=True, max_length=200, null=True)
    brand = models.CharField(blank=True, max_length=100, null=True)
    price = models.FloatField(null=True, blank=True)
    in_stock_quantity = models.IntegerField(default=0)
    image = models.ImageField(upload_to='uploads/products/')

    @staticmethod
    def get_all_products():
        return Product.objects.all()

    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Product.objects.filter(category = category_id)
        else:
            return Product.get_all_products();

