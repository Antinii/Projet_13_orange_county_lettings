from django.test import TestCase, RequestFactory, SimpleTestCase
from .models import Letting, Address
from django.urls import reverse, resolve
from .views import index, letting


class LettingModelTest(TestCase):
    """
    Test case for the Letting model.
    """

    def setUp(self):
        """
        Set up the test environment by creating necessary objects.

        This method is called before each test case is executed.

        Creates an Address object with the following attributes:
        - number: 123
        - street: "Main St"
        - city: "City"
        - state: "NY"
        - zip_code: 12345
        - country_iso_code: "USA"

        Creates a Letting object with the following attributes:
        - title: "Test Letting"
        - address: the previously created Address object
        """
        self.address = Address.objects.create(
            number=123,
            street="Main St",
            city="City",
            state="NY",
            zip_code=12345,
            country_iso_code="USA",
        )
        self.letting = Letting.objects.create(
            title="Test Letting", address=self.address
        )

    def test_letting_creation(self):
        """
        Test case for the creation of a letting.

        This test verifies that the title and address number of the letting are set correctly.

        """
        self.assertEqual(self.letting.title, "Test Letting")
        self.assertEqual(self.letting.address.number, 123)


class LettingViewsTest(TestCase):
    """
    Test case for the views related to lettings.
    """

    def setUp(self):
        """
        Set up the test environment before each test case.

        This method is called before each test case to set up any necessary
        objects or data. In this case, it creates a RequestFactory object,
        an Address object, and a Letting object for testing purposes.

        """
        self.factory = RequestFactory()
        self.address = Address.objects.create(
            number=123,
            street="Main St",
            city="City",
            state="NY",
            zip_code=12345,
            country_iso_code="USA",
        )
        self.letting = Letting.objects.create(
            title="Test Letting", address=self.address
        )

    def test_index_view(self):
        """
        Test case for the index view.

        This method tests the behavior of the index view by making a GET request to the "/lettings/" URL
        and asserting that the response status code is 200 (OK).

        """
        request = self.factory.get("/lettings/")
        response = index(request)
        self.assertEqual(response.status_code, 200)

    def test_letting_view(self):
        """
        Test case for the letting view.

        This method tests the behavior of the letting view by making a GET request
        to the specific letting URL and checking if the response status code is 200.

        """
        request = self.factory.get(f"/{self.letting.id}/")
        response = letting(request, letting_id=self.letting.id)
        self.assertEqual(response.status_code, 200)


class LettingURLTest(SimpleTestCase):
    """
    Test case for URL resolution in the Letting app.
    """

    def test_index_url_resolves(self):
        """
        Test that the URL for the 'lettings:letting' resolves to the correct view function.
        """
        url = reverse("lettings:letting")
        self.assertEqual(resolve(url).func, index)

    def test_letting_url_resolves(self):
        """
        Test case to check if the URL for the 'letting' view resolves correctly.
        """
        url = reverse("lettings:letting", args=[1])
        self.assertEqual(resolve(url).func, letting)


class IntegrationTest(TestCase):
    """
    A test case for integration testing of the Lettings application.
    """

    def setUp(self):
        """
        Set up the test environment before each test case.

        This method is called before each test case to set up any necessary objects or configurations.
        In this case, it creates a RequestFactory object, an Address object, and a Letting object.

        Args:
            self: The current instance of the test case.

        Returns:
            None
        """
        self.factory = RequestFactory()
        self.address = Address.objects.create(
            number=123,
            street="Main St",
            city="City",
            state="NY",
            zip_code=12345,
            country_iso_code="USA",
        )
        self.letting = Letting.objects.create(
            title="Test Letting", address=self.address
        )

    def test_index_view(self):
        """
        Test case for the index view.

        This method tests the behavior of the index view by making a GET request to the root URL ("/")
        and asserting that the response status code is 200 (OK). It also checks if the content of the
        response contains the title of the letting.

        """
        request = self.factory.get("/")
        response = index(request)
        self.assertEqual(response.status_code, 200)
        content = response.content.decode("utf-8")
        self.assertTrue(self.letting.title in content)

    def test_letting_view(self):
        """
        Test case for the letting view.

        This method tests the behavior of the letting view by making a GET request
        to the specific letting URL and checking if the response status code is 200.
        It also checks if the letting's title and address are present in the response content.

        """
        request = self.factory.get(f"/{self.letting.id}/")
        response = letting(request, letting_id=self.letting.id)
        self.assertEqual(response.status_code, 200)
        content = response.content.decode("utf-8")
        self.assertTrue(self.letting.title in content)
        self.assertTrue(str(self.address) in content)
