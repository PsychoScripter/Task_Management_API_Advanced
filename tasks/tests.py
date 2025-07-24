
from django.test import TestCase

# Create your tests here.
from rest_framework.test import APITestCase
from .models import Task, Project
from authentication.models import CustomUser
from django.urls import reverse
from rest_framework import status

class TaskAPITestCase(APITestCase):
    def setUp(self):
        User = CustomUser
        self.user = User.objects.create_user(username="testuser", password="testpass")

        self.project = Project.objects.create(title="Test Project", owner=self.user)
        self.task = Task.objects.create(title="Test Task", description="Sample description", project=self.project)

        self.client.force_authenticate(user=self.user)

    def test_project_list(self):
        Project.objects.create(title="Sample Project", owner=self.user)
        url = reverse('project-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('title' in response.data['results'][0])

    def test_task_list(self):
        url = reverse('task-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('title' in response.data['results'][0])

    def test_task_detail(self):
        url = reverse('task-detail', kwargs={'pk': self.task.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('title' in response.data)
