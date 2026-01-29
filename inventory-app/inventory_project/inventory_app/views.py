from django.shortcuts import render, get_object_or_404
from django.db import connection
from django.http import JsonResponse
from inventory_app.models import PhysicalProduct, DigitalProduct, Category


def product_list(request):
    physical_products = PhysicalProduct.objects.all()
    digital_products = DigitalProduct.objects.all()

    context = {
        'physical_products': physical_products,
        'digital_products': digital_products,
    }
    return render(request, 'product_list.html', context)


def product_detail(request, pk):
    # Try to get physical product first, then digital
    try:
        product = PhysicalProduct.objects.get(pk=pk)
    except PhysicalProduct.DoesNotExist:
        product = get_object_or_404(DigitalProduct, pk=pk)

    final_price = product.calculate_final_price()

    context = {
        'product': product,
        'final_price': final_price,
        'base_price': product.base_price,
        'stock': product.stock_quantity,
    }
    return render(request, 'product_detail.html', context)


def sql_queries_view(request):
    with connection.cursor() as cursor:
        # Query 1: Products with less than 10 units in stock
        query1 = """
        SELECT 
            id, 
            name, 
            stock_quantity, 
            base_price, 
            product_type,
            category_id
        FROM inventory_app_physicalproduct
        WHERE stock_quantity < 10
        UNION ALL
        SELECT 
            id, 
            name, 
            stock_quantity, 
            base_price, 
            product_type,
            category_id
        FROM inventory_app_digitalproduct
        WHERE stock_quantity < 10
        ORDER BY stock_quantity ASC
        """

        cursor.execute(query1)
        low_stock_products = cursor.fetchall()

        # Query 2: Average price by category
        query2 = """
        SELECT 
            c.name as category_name,
            AVG(pp.base_price) as avg_price,
            COUNT(pp.id) as product_count
        FROM inventory_app_category c
        LEFT JOIN inventory_app_physicalproduct pp ON c.id = pp.category_id
        GROUP BY c.name
        
        UNION ALL
        
        SELECT 
            c.name as category_name,
            AVG(dp.base_price) as avg_price,
            COUNT(dp.id) as product_count
        FROM inventory_app_category c
        LEFT JOIN inventory_app_digitalproduct dp ON c.id = dp.category_id
        WHERE dp.id IS NOT NULL
        GROUP BY c.name
        """

        cursor.execute(query2)
        avg_by_category = cursor.fetchall()

    context = {
        'low_stock_products': low_stock_products,
        'avg_by_category': avg_by_category,
    }
    return render(request, 'sql_queries.html', context)
