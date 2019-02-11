from django.contrib import admin

# Register your models here.
from .models import Stock

my_models = [Stock, ]

admin.site.register(my_models)
