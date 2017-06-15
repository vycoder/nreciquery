from django.db import models


class Ingredient(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Seasoning(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    name = models.CharField(max_length=500)
    description = models.TextField(default="")

    STARTER = 'ST'
    MAIN_DISH = 'MD'
    SIDE_DISH = 'SD'
    SNACK = 'SN'
    DESSERT = 'DS'
    TYPES = (
        (STARTER, 'Started'),
        (MAIN_DISH, 'Main Dish'),
        (SIDE_DISH, 'Side Dish'),
        (SNACK, 'Snack'),
        (DESSERT, 'Dessert'),
    )
    type = models.CharField(max_length=2, choices=TYPES, default=MAIN_DISH)

    ingredients = models.ManyToManyField(Ingredient)
    seasonings = models.ManyToManyField(Seasoning)
    ingredients_details = models.TextField(default="")
    directions = models.TextField(default="")
    image = models.TextField(default="default.svg")

    def __str__(self):
        return self.name