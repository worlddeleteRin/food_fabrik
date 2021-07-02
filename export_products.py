import os
import django
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'food_fabrik.settings')
django.setup()

from products.models import *
import pandas as pd

products = Product.objects.all()
d = pd.DataFrame(columns = {
    'name',
    'category',
    'price',
    'sale_price',
    'desc',
    'imgsrc',
})

for p in products:
    d = d.append({
        'name': p.name,
        'category': p.category.name,
        'price': p.price,
        'sale_price': p.sale_price,
        'desc': p.description,
        'imgsrc': 'https://food-fabrik.ru/static/images/products/' + p.imgsrc.name.split('/')[-1],
    }, ignore_index = True)
    
d.to_excel('exported_products.xlsx')
