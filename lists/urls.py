from django.urls import path
from lists import views

app_name = "lists"  # This is essential to namespace the URLs for this app

urlpatterns = [
    path("", views.index, name="index"),
    path("todolist/<int:todolist_id>/", views.todolist, name="todolist"),
    path("todolist/new/", views.new_todolist, name="new_todolist"),
    path("todolist/add/", views.add_todolist, name="add_todolist"),
    path("todo/add/<int:todolist_id>/", views.add_todo, name="add_todo"),
    path("todolists/", views.overview, name="overview"),
    path("todolist/delete/<int:todolist_id>/", views.delete_todolist, name="delete_todolist"),
    path('delete_task/<int:todo_id>/', views.delete_task, name='delete_task'),
    path('update_task/<int:task_id>/', views.update_task, name='update_task'),
]
