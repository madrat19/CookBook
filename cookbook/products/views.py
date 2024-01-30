from django.shortcuts import render
from .models import Recipe, Product, RecipeIngredient
from django.http import HttpResponse
from django.db import transaction
from django.db import connection

@transaction.atomic
def add_product_to_recipe(request):
    recipe_id = request.GET.get('recipe_id')
    product_id = request.GET.get('product_id')
    weight = request.GET.get('weight')

    try:
        recipe = Recipe.objects.get(id=recipe_id)
        product = Product.objects.get(id=product_id)

        # Пытаемся получить RecipeIngredient для данного рецепта и продукта
        recipe_ingredient = RecipeIngredient.objects.get(recipe=recipe, product=product)

        # Если получается, обновляем вес
        recipe_ingredient.weight_in_grams = weight
        recipe_ingredient.save()

    except Recipe.DoesNotExist:
        return HttpResponse({"error": "Recipe not found"}, status=404)
    except Product.DoesNotExist:
        return HttpResponse({"error": "Product not found"}, status=404)
    except RecipeIngredient.DoesNotExist:
        # Если RecipeIngredient не существует, создаем новый
        recipe_ingredient = RecipeIngredient(recipe=recipe, product=product, weight_in_grams=weight)
        recipe_ingredient.save()

    return HttpResponse({"success": "Product added to recipe successfully"}, status=200)



@transaction.atomic
def cook_recipe(request):
    recipe_id = request.GET.get('recipe_id')

    try:
        # Получаем объект рецепта по его идентификатору
        recipe = Recipe.objects.get(id=recipe_id)

        # Получаем все ингредиенты, связанные с рецептом
        recipe_ingredients = RecipeIngredient.objects.filter(recipe=recipe)
        print(recipe_ingredients)
        
        # Увеличиваем количество использований каждого ингредиента
        for recipe_ingredient in recipe_ingredients:
            recipe_ingredient.product.times_used += 1
            recipe_ingredient.product.save()
        return HttpResponse({"success": "Recipe cooked successfully"}, status=200)
        
    except Recipe.DoesNotExist:
        return HttpResponse({"error": "Recipe not found"}, status=404)
    

def show_recipes_without_product(request):
    product_id = request.GET.get('product_id')
    
    try:
        # Получаем объект продукта та по его идентификатору
        product = Product.objects.get(id=product_id)

        # Отбираем рецепты для фильтрации
        filtered_recipes = RecipeIngredient.objects.filter(product=product, weight_in_grams__gt=10).values('recipe')
        
        # Отбираем нужные рецепты
        recipes = Recipe.objects.exclude(pk__in = filtered_recipes)

        # Рендерим страницу с таблицой
        return render(request, 'recipes.html', {'product' : product.name, 'recipes': recipes})
    
    except Product.DoesNotExist:
        return HttpResponse({"error": "Product not found"}, status=404)
