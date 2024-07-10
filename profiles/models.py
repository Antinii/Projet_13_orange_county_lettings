from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    A model representing a user profile.

    Attributes:
        user (OneToOneField): The user associated with this profile.
        favorite_city (CharField): The user's favorite city, with a maximum
        length of 64 characters (optional).
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        """
        Returns a string representation of the profile.

        Returns:
            str: The username of the associated user.
        """
        return self.user.username

    class Meta:
        """
        Meta options for the Profile model.
        """
        verbose_name_plural = "Profiles"
