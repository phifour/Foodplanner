from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Ingredient, Recipe, Recipe_Ingredient_Mapping,Mealplan

admin.site.register(Ingredient)
admin.site.register(Recipe)
admin.site.register(Recipe_Ingredient_Mapping)
admin.site.register(Mealplan)