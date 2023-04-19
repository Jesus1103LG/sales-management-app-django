from .models import Product, Sale, Income
from rest_framework import viewsets, permissions
from .serializer import ProductSerializer, SaleSerializer, IncomeSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProductSerializer

class SaleViewSet(viewsets.ModelViewSet):
    queryset = Sale.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = SaleSerializer

class IncomeViewSet(viewsets.ModelViewSet):
    queryset = Income.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = IncomeSerializer