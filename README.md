# Поварская книга на django

## Описание 
Это приложение поварской книги, хранящее списки продуктов и рецептов, связь между ними, а также поддерживающее некоторые операции над этими данными.

## Установка и запуск 

* Клонировать репозиторий 
``` 
git clone https://github.com/madrat19/cookbook.git
```

* Установить зависимости 
```
pip install -r requirements.txt
```

* Провести миграции
```
python manage.py migrate
```

* Запустить сервер
```
python manage.py runserver
```

## HTTP функции

* add_product_to_recipe

```http
GET /add_product_to_recipe

Params:

{
  "recipe_id" : 2,
  "product_id" : 2,
  "weight" : 200
}
```

* cook_recipe

```http
GET /cook_recipe

Params:

{
  "recipe_id" : 1
}
```

* show_recipes_without_product

```http
GET /show_recipes_without_product

Params:

{
  "product_id" : 1
}
```
из адресной строки браузера:
```http
GET /show_recipes_without_product?product_id=1
```

## Админка
Также настроена django-админка, в которой можно смотреть и редактировать все базы данных


```http
GET /admin
```

## Тесты 
В файле test.py написано несколько простейших тестов для описанных выше функций. При желании в них можно помеять тестовые параметры.

  
