from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Sale, Income

# Create your views here.


def home(request):
    return render(request, 'home.html')

# PRODUCT FUNCTIONS


def products(request):
    products = Product.objects.all()
    return render(request, 'product/products.html', {'products': products})


def create_products(request):
    if request.method == 'GET':
        return render(request, 'product/create_product.html')
    else:
        try:
            us_price = request.POST['us_price']
            bs_price = request.POST['bs_price']
            product = Product.objects.create(
                product_name=request.POST['product_name'], us_price=float(us_price), bs_price=int(bs_price))
            return redirect('products')
        except ValueError:
            return render(request, 'product/create_product.html', {
                'error': 'Please provide valida data'
            })


def update_product(request, product_id):
    if request.method == 'GET':
        product = get_object_or_404(Product, pk=product_id)
        return render(request, 'product/product_detail.html', {'product_detail': product})
    else:
        try:
            product = get_object_or_404(Product, pk=product_id)
            product.product_name = request.POST['product_name']
            product.us_price = float(request.POST['us_price'])
            product.bs_price = int(request.POST['bs_price'])
            product.save()
            return redirect('products')
        except ValueError:
            product = get_object_or_404(Product, pk=product_id)
            return render(request, 'product/product_detail.html', {
                'product_detail': product,
                'error': 'Please provide valida data'
            })


def delete_products(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    try:
        if request.method == 'POST':
            product.delete()
            return redirect('products')
    except ValueError:
        return render(request, 'product/product_detail.html', {
            'error': 'Please provide valida data'
        })

# SALE FUNCTIONS


def sales(request):
    sales = Sale.objects.all()
    cantidad = len(sales)
    return render(request, 'sale/sales.html', {'sales': sales, 'cantidad': cantidad})


def create_sale(request):
    if request.method == 'GET':
        products = Product.objects.all()
        return render(request, 'sale/create_sale.html', {'products': products})
    else:
        try:
            amount = request.POST['amount']
            id_product = Product.objects.get(
                id=int(request.POST['id_product']))
            us_total = request.POST['us_total']
            bs_cash = request.POST['bs_cash']
            bs_transfer = request.POST['bs_transfer']
            sale = Sale.objects.create(
                amount=int(amount), id_product=id_product, us_total=float(us_total), bs_cash=int(bs_cash), bs_transfer=int(bs_transfer),)
            return redirect('sales')
        except ValueError:
            return render(request, 'sale/create_sale.html', {
                'error': 'Please provide valida data'
            })


def update_sale(request,sale_id):
    if request.method == 'GET':
        products = Product.objects.all()
        sale = get_object_or_404(Sale, pk=sale_id)
        return render(request, 'sale/sale_detail.html', {'sale_detail': sale,
        'products':products})
    else:
        try:
            products = Product.objects.all()
            sale = get_object_or_404(Sale, pk=sale_id)
            sale.amount = int(request.POST['amount'])
            sale.id_product = Product.objects.get(
                id=int(request.POST['id_product']))
            sale.us_total = float(request.POST['us_total'])
            sale.bs_cash = int(request.POST['bs_cash'])
            sale.bs_transfer = int(request.POST['bs_transfer'])
            sale.save()
            return redirect('sales')
        except ValueError:
            products = Product.objects.all()
            sale = get_object_or_404(Sale, pk=sale_id)
            return render(request, 'sale/sale_detail.html', {
                'sale_detail': sale,
                'products':products,
                'error': 'Please provide valida data'
            })


def delete_sale(request, sale_id):
    sale = get_object_or_404(Sale, pk=sale_id)
    try:
        if request.method == 'POST':
            sale.delete()
            return redirect('sales')
    except ValueError:
        return render(request, 'sale/sale_detail.html', {
            'error': 'Please provide valida data'
        })