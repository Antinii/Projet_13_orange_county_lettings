import logging
from django.shortcuts import render
from django.http import HttpResponseNotFound
from .models import Profile


logger = logging.getLogger(__name__)


# Sed placerat quam in pulvinar commodo. Nullam laoreet consectetur ex,
# sed consequat libero pulvinar eget. Fusc faucibus, urna quis auctor
# pharetra, massa dolor cursus neque, quis dictum lacus d
def index(request):
    """
    View function for the index page of profiles.

    Retrieves all profiles from the database and renders the index
    template with the list of profiles.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: The rendered index page with the context containing all profiles.
    """
    logger.debug('Profiles index view accessed')
    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles/index.html', context)


# Aliquam sed metus eget nisi tincidunt ornare accumsan eget lac
# laoreet neque quis, pellentesque dui. Nullam facilisis pharetra
# vulputate. Sed tincidunt, dolor id facilisis fringilla, eros leo
# tristique lacus, it. Nam aliquam dignissim congue. Pellentesque
# habitant morbi tristique senectus et netus et males
def profile(request, username):
    """
    View function for a single profile page.

    Retrieves a specific profile by username and renders the profile
    template with the profile's details.

    Args:
        request (HttpRequest): The request object.
        username (str): The username of the profile to be retrieved.

    Returns:
        HttpResponse: The rendered profile page with the context containing the profile.
    """
    try:
        profile = Profile.objects.get(user__username=username)
        context = {'profile': profile}
        logger.info(f'Profile view accessed for username: {username}')
        return render(request, 'profiles/profile.html', context)
    except Profile.DoesNotExist:
        logger.error(f'Profile not found for username: {username}')
        return HttpResponseNotFound('Profile not found')
