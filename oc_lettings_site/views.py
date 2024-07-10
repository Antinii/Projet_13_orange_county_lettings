from django.shortcuts import render


# Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque molestie quam
# lobortis leo consectetur ullamcorper non id est. Praesent dictum, nulla eget
# feugiat sagittis, sem mi convallis eros, vitae dapibus nisi lorem dapibus sem.
# Maecenas pharetra purus ipsum, eget consequat ipsum lobortis quis. Phasellus
# eleifend ex auctor venenatis tempus. Aliquam vitae erat ac orci placerat luctus.
# Nullam elementum urna nisi, pellentesque iaculis enim cursus in. Praesent volutpat
# porttitor magna, non finibus neque cursus id.
def index(request):
    """
    View function for the index page.

    Renders the index template.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: The rendered index page.
    """
    return render(request, 'index.html')


def handler404(request, exception):
    """
    View function for handling HTTP 404 errors.

    Renders the 404 error template.

    Args:
        request (HttpRequest): The request object.
        exception: The exception that triggered the 404 error.

    Returns:
        HttpResponse: The rendered 404 error page with HTTP status code 404.
    """
    return render(request, '404.html', status=404)


def handler500(request):
    """
    View function for handling HTTP 500 errors.

    Renders the 500 error template.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: The rendered 500 error page with HTTP status code 500.
    """
    return render(request, '500.html', status=500)
