from django.contrib import admin
from inventory_app.models import Category, PhysicalProduct, DigitalProduct


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    search_fields = ['name']


@admin.register(PhysicalProduct)
class PhysicalProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'base_price', 'stock_quantity', 'weight']
    list_filter = ['category', 'created_at']
    search_fields = ['name', 'description']
    readonly_fields = ['created_at', 'updated_at']
    fieldsets = (
        ('Product Information', {
            'fields': ('name', 'description', 'category', 'product_type')
        }),
        ('Pricing & Stock', {
            'fields': ('_base_price', '_stock_quantity')
        }),
        ('Physical Specifications', {
            'fields': ('weight', 'dimensions')
        }),
        ('Metadata', {
            'fields': ('created_at', 'updated_at')
        }),
    )

    def _base_price(self, obj):
        return obj.base_price
    _base_price.short_description = "Base Price"

    def _stock_quantity(self, obj):
        return obj.stock_quantity
    _stock_quantity.short_description = "Stock Quantity"


@admin.register(DigitalProduct)
class DigitalProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'base_price', 'stock_quantity', 'license_type']
    list_filter = ['category', 'license_type', 'created_at']
    search_fields = ['name', 'description']
    readonly_fields = ['created_at', 'updated_at']
    fieldsets = (
        ('Product Information', {
            'fields': ('name', 'description', 'category', 'product_type')
        }),
        ('Pricing & Stock', {
            'fields': ('_base_price', '_stock_quantity')
        }),
        ('Digital Specifications', {
            'fields': ('file_size', 'download_url', 'license_type')
        }),
        ('Metadata', {
            'fields': ('created_at', 'updated_at')
        }),
    )

    def _base_price(self, obj):
        return obj.base_price
    _base_price.short_description = "Base Price"

    def _stock_quantity(self, obj):
        return obj.stock_quantity
    _stock_quantity.short_description = "Stock Quantity"
