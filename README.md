# Django Tree Menu

Django-приложение с древовидным меню, редактируемым через стандартную админку.  
Меню поддерживает вложенность, активные пункты, несколько разных меню на сайте и легко настраивается.

### 1. Клонируйте репозиторий

```bash
git clone git@github.com:Faithdev21/uptrade.git
cd uptrade
```

### 2. Установите зависимости

```bash
python -m venv venv
source venv/bin/activate  # для Windows: source venv/Scripts/activate
pip install -r requirements.txt
```

### 3. Примените миграции

```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Загрузите тестовые данные (меню и пункты меню)

```bash
python manage.py loaddata tree_menu/fixtures/initial_data.json
```

### 5. Создайте суперпользователя

```bash
python manage.py createsuperuser
```

### 6. Запустите сервер

```bash
python manage.py runserver
```

### 7. Откройте сайт

Админка: http://127.0.0.1:8000/admin/
Главная: http://127.0.0.1:8000/

## Как пользоваться

Меню и пункты меню редактируются через админку Django.

Для вывода меню на странице используйте template tag:

```bash
{% load tree_menu_tags %}
{% draw_menu 'main_menu' %}
{% draw_menu 'footer_menu' %}
```

Все шаблоны страниц наследуют base.html.

Структура меню и вложенность настраиваются через поле Parent у пункта меню.

## Как добавить или изменить меню

1. В админке создайте новое меню (например, footer_menu).
2. Добавьте пункты меню, выбрав нужное меню и, при необходимости, родителя для вложенности.
3. Для вывода меню на сайте используйте тег {% draw_menu 'имя_меню' %} в нужном шаблоне.
