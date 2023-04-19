from django.db import models
import datetime

# Create your models here.

class Product(models.Model):
    product_name = models.CharField(max_length=100)
    us_price = models.FloatField()
    bs_price = models.IntegerField()

    def __str__(self):
        return self.product_name

class Sale(models.Model):
    amount = models.IntegerField(default=1)
    id_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    us_total = models.FloatField(null=True)
    bs_cash = models.IntegerField(null=True)
    bs_transfer = models.IntegerField(null=True)
    date_sale = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.id_product.product_name

class Income(models.Model):
    day_income = models.DateTimeField(datetime.date.today)
    us_total = models.FloatField()
    bs_total = models.IntegerField()
    id_sale = models.ForeignKey(Sale, on_delete=models.CASCADE)

    def __str__(self):
        return self.day_income