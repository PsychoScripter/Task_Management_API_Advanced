
from django.test import TestCase

# Create your tests here.
from rest_framework.test import APITestCase
from .models import Task

from django.urls import reverse
from rest_framework import status

class TaskAPITestCase(APITestCase):
    def setUp(self):
        self.task = Task.objects.create(title="Test Task", description="Sample description")

    def test_project_list(self):
        url = reverse('project-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('title' in response.data[0])

    def test_task_list(self):
        url = reverse('task-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('title' in response.data[0])

    def test_task_detail(self):
        url = reverse('task-detail', kwargs={'pk': self.task.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('title' in response.data[0])
