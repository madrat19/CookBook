import requests

'''# Тест функции 'add_product_to_recipe'
url = 'http://127.0.0.1:8000/add_product_to_recipe'
# Можно заменить тестовые параметры здесь:
params = {'recipe_id' : 2, 'product_id' : 2, 'weight' : 200}
response = requests.get(url, params=params)
print(response.status_code)'''

'''# Тест функции 'cook_recipe'
url = 'http://127.0.0.1:8000/cook_recipe'
# Можно заменить тестовые параметры здесь:
params = {'recipe_id' : 1}
response = requests.get(url, params=params)
print(response.status_code)'''



url = 'http://127.0.0.1:8000/show_recipes_without_product'
# Можно заменить тестовые параметры здесь:
params = {'product_id' : 1}
response = requests.get(url, params=params)
print(response.status_code)