from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Profile
from unittest.mock import patch


class ProfileModelTest(TestCase):
    """
    Test cases for the Profile model.
    """
    def setUp(self):
        """
        Set up a sample User and Profile object for testing.
        """
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.profile = Profile.objects.create(user=self.user, favorite_city='Test City')

    def test_profile_str(self):
        """
        Test the string representation of the Profile model.
        """
        self.assertEqual(str(self.profile), 'testuser')

    def test_profile_fields(self):
        """
        Test fields of the Profile model.
        """
        self.assertEqual(self.profile.user, self.user)
        self.assertEqual(self.profile.favorite_city, 'Test City')


class ProfileViewTests(TestCase):
    """
    Test case for profiles view.
    """
    def setUp(self):
        """
        Set up a sample Profile object with an associated user for testing views.
        """
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.profile = Profile.objects.create(user=self.user, favorite_city='Test City')

    @patch('profiles.views.logger')
    def test_index_view(self, mock_logger):
        """
        Test the index view of Profile.
        """
        response = self.client.get(reverse('profiles:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'testuser')
        self.assertTemplateUsed(response, 'profiles/index.html')
        mock_logger.debug.assert_called_with('Profiles index view accessed')

    @patch('profiles.views.logger')
    def test_profile_view(self, mock_logger):
        """
        Test the profiles detail view of Profile.
        """
        response = self.client.get(reverse('profiles:profile', args=[self.user.username]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'testuser')
        self.assertContains(response, 'Test City')
        self.assertTemplateUsed(response, 'profiles/profile.html')
        mock_logger.info.assert_called_with
        (f'Profile view accessed for username: {self.user.username}')

    @patch('profiles.views.logger')
    def test_profile_view_not_found(self, mock_logger):
        """
        Test the profile detail view if not found.
        """
        response = self.client.get(reverse('profiles:profile', args=['nonexistentuser']))
        self.assertEqual(response.status_code, 404)
        mock_logger.error.assert_called_with('Profile not found for username: nonexistentuser')
