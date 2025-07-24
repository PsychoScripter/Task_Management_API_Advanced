from django.urls import path
from .views import TaskListView, TaskDetailView, ProjectListView

urlpatterns = [
    path('', ProjectListView.as_view(), name='project-list'),
    path('tasks/', TaskListView.as_view(), name='task-list'),
    path('tasks/<int:id>/', TaskDetailView.as_view(), name='task-detail'),
]