from django.contrib import admin
from products.models import Products

models = [Products]
admin.site.register(models)

