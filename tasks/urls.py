from django.urls import path
from .views import TasksListCreateView

urlpatterns = [
    path('tasks/', TasksListCreateView.as_view(), name='task-list-create'),
]