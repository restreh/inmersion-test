from django.contrib import admin
from django.urls import path, include
from inventory_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.product_list, name='product_list'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('sql-queries/', views.sql_queries_view, name='sql_queries'),
]
