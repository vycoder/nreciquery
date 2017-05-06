from django.contrib import admin
from .models import Ingredient, Recipe, Condiment
# Register your models here.

admin.site.register(Ingredient)
admin.site.register(Condiment)
admin.site.register(Recipe)
