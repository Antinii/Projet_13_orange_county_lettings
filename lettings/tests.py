from django.test import TestCase
from django.urls import reverse
from .models import Address, Letting


class AddressModelTest(TestCase):
    """
    Test cases for Address model.
    """
    def setUp(self):
        """
        Set up a sample Address object for testing.
        """
        self.address = Address.objects.create(
            number=123,
            street="Sample Street",
            city="Sample City",
            state="SC",
            zip_code=12345,
            country_iso_code="USA"
        )

    def test_address_str(self):
        """
        Test the string representation of Address model.
        """
        self.assertEqual(str(self.address), '123 Sample Street')

    def test_address_fields(self):
        """"
        Test each field of the Address model.
        """
        self.assertEqual(self.address.number, 123)
        self.assertEqual(self.address.street, "Sample Street")
        self.assertEqual(self.address.city, "Sample City")
        self.assertEqual(self.address.state, "SC")
        self.assertEqual(self.address.zip_code, 12345)
        self.assertEqual(self.address.country_iso_code, "USA")


class LettingModelTest(TestCase):
    """
    Test cases for Letting model.
    """
    def setUp(self):
        """
        Set up a sample Letting object with an associated Address for testing.
        """
        self.address = Address.objects.create(
            number=123,
            street="Sample Street",
            city="Sample City",
            state="SC",
            zip_code=12345,
            country_iso_code="USA"
        )
        self.letting = Letting.objects.create(
            title="Sample Letting",
            address=self.address
        )

    def test_letting_str(self):
        """
        Test the string representation of Letting model.
        """
        self.assertEqual(str(self.letting), 'Sample Letting')

    def test_letting_fields(self):
        """
        Test fields of the Letting model.
        """
        self.assertEqual(self.letting.title, "Sample Letting")
        self.assertEqual(self.letting.address, self.address)


class LettingViewTests(TestCase):
    """
    Test cases for Letting views.
    """
    def setUp(self):
        """
        Set up a sample Letting object with an associated Address for testing views.
        """
        self.address = Address.objects.create(
            number=123,
            street="Sample Street",
            city="Sample City",
            state="SC",
            zip_code=12345,
            country_iso_code="USA"
        )
        self.letting = Letting.objects.create(
            title="Sample Letting",
            address=self.address
        )

    def test_index_view(self):
        """
        Test the index view of Letting.
        """
        response = self.client.get(reverse('lettings:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Sample Letting")
        self.assertTemplateUsed(response, 'lettings/index.html')

    def test_letting_view(self):
        """"
        Test the letting detail view of Letting.
        """
        response = self.client.get(reverse('lettings:letting', args=[self.letting.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Sample Letting")
        self.assertContains(response, "123 Sample Street")
        self.assertTemplateUsed(response, 'lettings/letting.html')
