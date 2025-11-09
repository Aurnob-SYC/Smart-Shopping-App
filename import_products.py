import os
import django
import pandas as pd

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "smart_shopping_app.settings")
django.setup()

from product_list_smart_suggestion.models import Product

CSV_PATH = r"C:/Users/a2i/Downloads/FoodData_Central_csv_2025-04-24/food.csv"

df = pd.read_csv(CSV_PATH)

descriptions = df["description"].dropna()

items = []
for desc in descriptions:
    parts = [p.strip().lower() for p in desc.split(',')]
    items.extend(parts)

unique_items = {i[:500] for i in items if i}   # truncate long strings

print("Unique items:", len(unique_items))

existing = set(Product.objects.values_list("name", flat=True))

new_products = [Product(name=item) for item in unique_items if item not in existing]

Product.objects.bulk_create(new_products, ignore_conflicts=True)

print("Inserted:", len(new_products))
