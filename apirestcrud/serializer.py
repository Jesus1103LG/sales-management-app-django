from rest_framework import serializers
from .models import Product, Sale, Income

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id','product_name','us_price','bs_price')

class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = ('id','amount','id_product','us_total','bs_cash','bs_transfer','date_sale')

class IncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Income
        fields = ('id','day_income','us_total','bs_total','id_sale')