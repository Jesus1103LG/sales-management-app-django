from django.contrib import admin
from .models import Product, Sale, Income

# Register your models here.

admin.site.register(Product)
admin.site.register(Sale)
admin.site.register(Income)