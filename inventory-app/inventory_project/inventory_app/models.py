from django.db import models
from django.core.exceptions import ValidationError
from decimal import Decimal


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"


class Product(models.Model):
    PRODUCT_TYPE_CHOICES = [
        ('physical', 'Physical Product'),
        ('digital', 'Digital Product'),
    ]

    name = models.CharField(max_length=200)
    description = models.TextField()
    _base_price = models.DecimalField(max_digits=10, decimal_places=2, db_column='base_price')
    _stock_quantity = models.IntegerField(db_column='stock_quantity', default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    product_type = models.CharField(max_length=10, choices=PRODUCT_TYPE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

    @property
    def base_price(self):
        return self._base_price

    @base_price.setter
    def base_price(self, value):
        if value < 0:
            raise ValidationError("Price cannot be negative")
        self._base_price = value

    @property
    def stock_quantity(self):
        return self._stock_quantity

    @stock_quantity.setter
    def stock_quantity(self, value):
        if value < 0:
            raise ValidationError("Stock quantity cannot be negative")
        self._stock_quantity = value

    def calculate_final_price(self):
        return self._base_price

    def check_margin_alert(self, final_price):
        if final_price < Decimal('5000.00'):
            print(f"MARGIN REVIEW REQUIRED: Product '{self.name}' has final price {final_price}")
            return True
        return False


class PhysicalProduct(Product):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='physical_products')
    weight = models.DecimalField(max_digits=10, decimal_places=2, help_text="Weight in kg")
    dimensions = models.CharField(max_length=100, blank=True, help_text="Length x Width x Height")

    def __str__(self):
        return f"[PHYSICAL] {self.name}"

    def calculate_final_price(self):
        price = Decimal(str(self._base_price))

        # Apply additional 5% discount if stock > 50
        if self._stock_quantity > 50:
            price = price * Decimal('0.95')

        self.check_margin_alert(price)
        return price


class DigitalProduct(Product):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='digital_products')
    file_size = models.CharField(max_length=100, help_text="File size in MB")
    download_url = models.URLField()
    license_type = models.CharField(
        max_length=50,
        choices=[
            ('single', 'Single User'),
            ('team', 'Team License'),
            ('enterprise', 'Enterprise'),
        ]
    )

    def __str__(self):
        return f"[DIGITAL] {self.name}"

    def calculate_final_price(self):
        price = Decimal(str(self._base_price))

        # Apply 15% discount for digital products
        price = price * Decimal('0.85')

        # Apply additional 5% discount if stock > 50
        if self._stock_quantity > 50:
            price = price * Decimal('0.95')

        self.check_margin_alert(price)
        return price
