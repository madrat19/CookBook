from django.urls import path, include
from . import views

urlpatterns = [
    path('add_product_to_recipe', views.add_product_to_recipe),
    path('cook_recipe', views.cook_recipe),
    path('show_recipes_without_product', views.show_recipes_without_product)
]
