from django.contrib import admin
from django.urls import path, include
from apirestcrud import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('manager/', include('apirestcrud.urls')),
    path('', views.home, name='home'),
    #products routes
    path('products/', views.products, name='products'),
    path('products/create/', views.create_products, name='create_product'),
    path('products/<int:product_id>/', views.update_product, name='update_product'),
    path('products/<int:product_id>/delete', views.delete_products, name='delete_product'),
    #sales routes
    path('sales/', views.sales, name='sales'),
    path('sales/create/', views.create_sale, name='create_sale'),
    path('sales/<int:sale_id>/', views.update_sale, name='update_sale'),
    path('sales/<int:sale_id>/delete', views.delete_sale, name='delete_sale'),
]
