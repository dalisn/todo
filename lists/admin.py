from django.contrib import admin

# Register your models here.
from .models import Todo, TodoList


admin.site.register(Todo)
admin.site.register(TodoList)
