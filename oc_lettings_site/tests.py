from django.test import TestCase
from django.urls import reverse


class TestHomePage(TestCase):
    """
    A test case for the home page of the website.

    This test case contains multiple test methods to verify the functionality
    and behavior of different pages on the website.

    Test methods:
    - test_dummy: A dummy test method that always passes.
    - test_home_page: Test method to check the status code of the home page.
    - test_admin_page: Test method to check the status code of the admin page.
    - test_profile_page: Test method to check the status code of the profile page.
    - test_lettings_page: Test method to check the status code of the lettings page.
    - test_404_page: Test method to check the status code of the 404 error page.
    - test_500_page: Test method to check the status code of the 500 error page.
    """

    def test_dummy(self):
        """
        This is a dummy test method.
        It asserts that the value 1 is True.
        """
        assert 1

    def test_home_page(self):
        """
        Test case for the home page.

        This method sends a GET request to the "index" URL and checks if the response
        status code is 200 (OK).

        """
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)

    def test_admin_page(self):
        """
        Test case for checking the status code of the admin page.

        This test sends a GET request to the "/admin/" URL and checks if the response
        status code is equal to 302 (redirect). This ensures that the admin page is
        accessible and redirects the user to the appropriate location.

        """
        response = self.client.get("/admin/")
        self.assertEqual(response.status_code, 302)

    def test_profile_page(self):
        """
        Test case for the profile page.

        This method sends a GET request to the "/profiles/" URL and checks if the response
        status code is 200 (OK).

        """
        response = self.client.get("/profiles/")
        self.assertEqual(response.status_code, 200)

    def test_lettings_page(self):
        """
        Test case for the lettings page.

        This method sends a GET request to the "/lettings/" URL and checks if the response
        status code is 200 (OK).

        """
        response = self.client.get("/lettings/")
        self.assertEqual(response.status_code, 200)

    def test_404_page(self):
        """
        Test case for the 404 error page.

        This method sends a GET request to the "/error/404/" URL and checks if the response
        status code is 404 (Not Found).

        """
        response = self.client.get("/error/404/")
        self.assertEqual(response.status_code, 404)

    def test_500_page(self):
        """
        Test case for the 500 error page.

        This method sends a GET request to the "/error/500/" URL and checks if the response
        status code is 500 (Internal Server Error).

        """
        response = self.client.get("/error/500/")
        self.assertEqual(response.status_code, 500)
