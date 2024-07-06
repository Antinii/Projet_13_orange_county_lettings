from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator


class Address(models.Model):
    """
    A model representing an address.

    Attributes:
        number (PositiveIntegerField): The street number, must be a positive integer up to 9999.
        street (CharField): The name of the street, with a maximum length of 64 characters.
        city (CharField): The name of the city, with a maximum length of 64 characters.
        state (CharField): The two-letter state code, exactly 2 characters long.
        zip_code (PositiveIntegerField): The ZIP code, must be a positive integer up to 99999.
        country_iso_code (CharField): The ISO country code, exactly 3 characters long.
    """
    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(max_length=3, validators=[MinLengthValidator(3)])

    def __str__(self):
        """
        Returns a string representation of the address.

        Returns:
            str: The street number and name.
        """
        return f'{self.number} {self.street}'

    class Meta:
        """
        Meta options for the Address model.
        """
        verbose_name_plural = "Addresses"


class Letting(models.Model):
    """
    A model representing a letting.

    Attributes:
        title (CharField): The title of the letting, with a maximum length of 256 characters.
        address (OneToOneField): A one-to-one relationship with the Address model.
    """
    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        """
        Returns a string representation of the letting.

        Returns:
            str: The title of the letting.
        """
        return self.title

    class Meta:
        """
        Meta options for the Letting model.
        """
        verbose_name_plural = "Lettings"
