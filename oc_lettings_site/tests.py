from django.test import TestCase, Client
from django.urls import reverse
from django.http import HttpRequest
from django.conf import settings


class IndexViewTest(TestCase):
    """
    Test cases for the index view.
    """
    def setUp(self):
        """
        Set up the client for making requests.
        """
        self.client = Client()

    def test_index_view_status_code(self):
        """
        Test the status code of the index view.
        """
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_index_view_template(self):
        """
        Test the template used by the index view.
        """
        response = self.client.get(reverse('index'))
        self.assertTemplateUsed(response, 'index.html')


class ErrorViewsTest(TestCase):
    """
    Test cases for error views (e.g., 404 page).
    """
    def setUp(self):
        """
        Set up the client for making requests.
        """
        self.client = Client()

    def test_404_view(self):
        """
        Test the handling of a non-existent page (404 error).
        """
        response = self.client.get('/non-existent-page/')
        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, '404.html')

    def test_500_view(self):
        """
        Test the handling of a server error page (500 error).
        """
        response = self.client.get('/error/500/')
        self.assertTemplateUsed(response, '500.html')
