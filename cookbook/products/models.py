from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255, unique=True)
    times_used = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    name = models.CharField(max_length=255)
    ingredients = models.ManyToManyField(Product, through='RecipeIngredient')

    def __str__(self):
        return self.name

class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    weight_in_grams = models.IntegerField()

    def __str__(self):
        return str(self.recipe.name) + ' - ' + str(self.product.name) + ' - ' + str(self.weight_in_grams) + 'g'

