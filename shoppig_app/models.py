from django.db import models

# Create your models here.

class Products(models.Model):
    product_name=models.CharField(max_length=200)
    product_price=models.FloatField()
    product_quantity=models.PositiveIntegerField()

class Order(models.Model):
    product_name=models.CharField(max_length=200)
    Invoice_ID=models.CharField(max_length=200)
    product_price=models.FloatField()
    product_quantity=models.PositiveIntegerField()
    date_of_insertion=models.DateField(auto_now_add=True)
    user_name=models.CharField(max_length=200)
    user_consumer=models.CharField(max_length=200)
    class Meta:
        db_table = "orders"
