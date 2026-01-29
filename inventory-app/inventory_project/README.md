# Inventory Management Application

I decided to make a Django-based inventory management system.

## Quick Start

1. Create virtual environment:
```powershell
python -m venv .venv
```

2. Activate virtual environment:
```powershell
.\.venv\Scripts\Activate.ps1
```

3. Install dependencies:
```powershell
pip install -r requirements.txt
```

4. Run the server:
```powershell
python manage.py runserver
```

5. Open browser to `http://localhost:8000`

## Features

- Product inventory management (physical and digital)
- Dynamic pricing with automatic stock-based discounts
- Admin panel: `http://localhost:8000/admin/` (admin/admin)
- SQL queries: `http://localhost:8000/sql_queries/`
- Pre-loaded with 10 products across 4 categories
