from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated

from tasks.models import Task, Project
from tasks.serializers import TaskSerializer, ProjectSerializer

from tasks.permissions import IsOwnerOrReadOnly
# Create your views here

class TaskPagination(PageNumberPagination):
    page_size = 4

class TaskListView(ListCreateAPIView):
    def get_queryset(self):
        completed = self.request.query_params.get('completed', None)
        if completed is not None:
            return Task.objects.filter(completed=completed)
        return Task.objects.all()

    queryset = Task.objects.all().order_by('-created_at')
    serializer_class = TaskSerializer

    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['status', 'priority',]
    search_fields = ['title']

    pagination_class = TaskPagination

    permission_classes = [IsOwnerOrReadOnly]

class TaskDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsOwnerOrReadOnly]

class ProjectListView(ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsOwnerOrReadOnly]

class ProjectDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsOwnerOrReadOnly]



