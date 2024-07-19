import logging
from django.shortcuts import render
from django.http import HttpResponseNotFound
from .models import Letting


logger = logging.getLogger(__name__)


# Aenean leo magna, vestibulum et tincidunt fermentum, consectetur quis velit.
# Sed non placerat massa. Integer est nunc, pulvinar a tempor et, bibendum id
# arcu. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere
# cubilia curae; Cras eget scelerisque
def index(request):
    """
    View function for the index page.

    This view retrieves all lettings from the database and renders the
    index template with the list of lettings.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: The rendered index page with the context containing all lettings.
    """
    logger.debug('Lettings index view accessed')
    lettings_list = Letting.objects.all()
    context = {'lettings_list': lettings_list}
    return render(request, 'lettings/index.html', context)


# Cras ultricies dignissim purus, vitae hendrerit ex varius non. In accumsan porta
# nisl id eleifend. Praesent dignissim, odio eu consequat pretium, purus urna vulputate
# arcu, vitae efficitur lacus justo nec purus. Aenean finibus faucibus lectus at porta.
# Maecenas auctor, est ut luctus congue, dui enim mattis enim, ac condimentum velit
# libero in magna. Suspendisse potenti. In tempus a nisi sed laoreet.
# Suspendisse porta dui eget sem accumsan interdum. Ut quis urna pellentesque justo
# mattis ullamcorper ac non tellus. In tristique mauris eu velit fermentum, tempus pharetra
# est luctus. Vivamus consequat aliquam libero, eget bibendum lorem. Sed non dolor risus.
# Mauris condimentum auctor elementum. Donec quis nisi ligula. Integer vehicula tincidunt
# enim, ac lacinia augue pulvinar sit amet.
def letting(request, letting_id):
    """
    View function for a single letting page.

    This view retrieves a specific letting by its ID and renders the letting template
    with the letting's details.

    Args:
        request (HttpRequest): The request object.
        letting_id (int): The ID of the letting to be retrieved.

    Returns:
        HttpResponse: The rendered letting page with the context containing the letting's
        title and address.
    """
    try:
        letting = Letting.objects.get(id=letting_id)
        context = {
            'title': letting.title,
            'address': letting.address,
        }
        logger.info(f'Letting view accessed for letting_id: {letting_id}')
        return render(request, 'lettings/letting.html', context)
    except Letting.DoesNotExist:
        logger.error(f'Letting not found for letting_id: {letting_id}')
        return HttpResponseNotFound('Letting not found')
