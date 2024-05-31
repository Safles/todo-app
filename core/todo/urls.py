from django.urls import path
from todo.views import todo, getTodoByID

urlpatterns = [
    path('todo/', todo),
    path('edit_todo/<int:id>', getTodoByID)
]
