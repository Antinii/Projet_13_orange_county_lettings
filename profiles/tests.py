from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Profile


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
    Test cases for Profile views.
    """
    def setUp(self):
        """
        Set up the client and a sample User with Profile object for testing views.
        """
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.profile = Profile.objects.create(user=self.user, favorite_city='Test City')

    def test_index_view(self):
        """
        Test the index view of Profile.
        """
        response = self.client.get(reverse('profiles:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'testuser')
        self.assertTemplateUsed(response, 'profiles/index.html')

    def test_profile_view(self):
        """
        Test the profile detail view of Profile.
        """
        response = self.client.get(reverse('profiles:profile', args=[self.user.username]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'testuser')
        self.assertContains(response, 'Test City')
        self.assertTemplateUsed(response, 'profiles/profile.html')
