from django.shortcuts import render
from .models import Letting


def index(request):
    """
    View function for the index page.

    This view retrieves all lettings from the database and renders the index template with the list of lettings.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: The rendered index page with the context containing all lettings.
    """
    lettings_list = Letting.objects.all()
    context = {'lettings_list': lettings_list}
    return render(request, 'lettings/index.html', context)


def letting(request, letting_id):
    """
    View function for a single letting page.

    This view retrieves a specific letting by its ID and renders the letting template with the letting's details.

    Args:
        request (HttpRequest): The request object.
        letting_id (int): The ID of the letting to be retrieved.

    Returns:
        HttpResponse: The rendered letting page with the context containing the letting's title and address.
    """
    letting = Letting.objects.get(id=letting_id)
    context = {
        'title': letting.title,
        'address': letting.address,
    }
    return render(request, 'lettings/letting.html', context)
