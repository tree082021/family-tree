from django.contrib import admin
# Импорт модели
from .models import Person

# Добавление модели на главную страницу интерфейса администратора
admin.site.register(Person)
