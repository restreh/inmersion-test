from django.core.management.base import BaseCommand
from decimal import Decimal
from inventory_app.models import Category, PhysicalProduct, DigitalProduct


class Command(BaseCommand):
    help = 'Populate database with sample inventory data'

    def handle(self, *args, **options):
        self.stdout.write("Creating sample data...")

        # Create Categories
        categories_data = [
            {'name': 'Electronics', 'description': 'Electronic devices and accessories'},
            {'name': 'Software', 'description': 'Software licenses and applications'},
            {'name': 'Books', 'description': 'Digital and physical books'},
            {'name': 'Accessories', 'description': 'Computer and tech accessories'},
        ]

        categories = {}
        for cat_data in categories_data:
            cat, created = Category.objects.get_or_create(**cat_data)
            categories[cat_data['name']] = cat
            if created:
                self.stdout.write(self.style.SUCCESS(f'✓ Created category: {cat.name}'))

        # Create Physical Products
        physical_products_data = [
            {
                'name': 'Gaming Laptop',
                'description': 'High-performance laptop for gaming and professional work',
                '_base_price': Decimal('8500.00'),
                '_stock_quantity': 15,
                'category': categories['Electronics'],
                'weight': Decimal('2.5'),
                'dimensions': '35cm x 25cm x 2cm',
            },
            {
                'name': 'Mechanical Keyboard',
                'description': 'RGB mechanical keyboard with custom switches',
                '_base_price': Decimal('3200.00'),
                '_stock_quantity': 45,
                'category': categories['Accessories'],
                'weight': Decimal('1.2'),
                'dimensions': '45cm x 15cm x 3cm',
            },
            {
                'name': 'USB-C Hub',
                'description': 'Multi-port USB-C hub with HDMI and card reader',
                '_base_price': Decimal('4500.00'),
                '_stock_quantity': 5,
                'category': categories['Accessories'],
                'weight': Decimal('0.2'),
                'dimensions': '10cm x 5cm x 2cm',
            },
            {
                'name': 'Wireless Mouse',
                'description': 'Ergonomic wireless mouse with long battery life',
                '_base_price': Decimal('2800.00'),
                '_stock_quantity': 75,
                'category': categories['Accessories'],
                'weight': Decimal('0.1'),
                'dimensions': '6cm x 3cm x 2cm',
            },
            {
                'name': 'Monitor 4K',
                'description': '32-inch 4K UltraHD monitor',
                '_base_price': Decimal('12000.00'),
                '_stock_quantity': 8,
                'category': categories['Electronics'],
                'weight': Decimal('8.5'),
                'dimensions': '70cm x 50cm x 20cm',
            },
        ]

        for product_data in physical_products_data:
            product, created = PhysicalProduct.objects.get_or_create(
                name=product_data['name'],
                defaults=product_data
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'✓ Created physical product: {product.name}'))

        # Create Digital Products
        digital_products_data = [
            {
                'name': 'Microsoft Office 365',
                'description': 'Annual subscription to Microsoft Office Suite',
                '_base_price': Decimal('7000.00'),
                '_stock_quantity': 200,
                'category': categories['Software'],
                'file_size': '2500',
                'download_url': 'https://example.com/office365',
                'license_type': 'team',
            },
            {
                'name': 'Adobe Creative Cloud',
                'description': 'Complete creative suite subscription',
                '_base_price': Decimal('8500.00'),
                '_stock_quantity': 120,
                'category': categories['Software'],
                'file_size': '5000',
                'download_url': 'https://example.com/adobe',
                'license_type': 'team',
            },
            {
                'name': 'Python Programming E-Book',
                'description': 'Comprehensive Python programming guide',
                '_base_price': Decimal('3000.00'),
                '_stock_quantity': 8,
                'category': categories['Books'],
                'file_size': '50',
                'download_url': 'https://example.com/python-ebook',
                'license_type': 'single',
            },
            {
                'name': 'Django Web Development Course',
                'description': 'Complete Django web development course',
                '_base_price': Decimal('4500.00'),
                '_stock_quantity': 150,
                'category': categories['Software'],
                'file_size': '3000',
                'download_url': 'https://example.com/django-course',
                'license_type': 'single',
            },
            {
                'name': 'Cybersecurity Handbook',
                'description': 'Digital handbook for cybersecurity professionals',
                '_base_price': Decimal('2500.00'),
                '_stock_quantity': 3,
                'category': categories['Books'],
                'file_size': '100',
                'download_url': 'https://example.com/cybersecurity',
                'license_type': 'single',
            },
        ]

        for product_data in digital_products_data:
            product, created = DigitalProduct.objects.get_or_create(
                name=product_data['name'],
                defaults=product_data
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'✓ Created digital product: {product.name}'))

        self.stdout.write(self.style.SUCCESS('\n✅ Sample data creation completed!'))
