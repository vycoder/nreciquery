from django.contrib import admin
from .models import Ingredient, Recipe, Seasoning
# Register your models here.

admin.site.register(Ingredient)
admin.site.register(Seasoning)
admin.site.register(Recipe)
