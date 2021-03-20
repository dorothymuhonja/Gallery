from django.shortcuts import render
from .models import Image, Location


def index(request):
    images = Image.objects.all()
    locations = Location.get_locations()
    return render(request, 'index.html', {'images': images[::-1], 'locations': locations})

def image_location(request, location):
    images = Image.filter_by_location(location)
    return render(request, 'location.html', {'location_images': images})


def search_image(request):
    if 'imagesearch' in request.GET and request.GET['imagesearch']:
        category = request.GET.get('imagesearch')
        searched_images = Image.search_by_category(category)
        message = f'{category}'
        return render(request, 'search_image.html', {'message': message})

    else:
        message = "You haven't searched for any images"
        return render(request, 'search_image.html', {'messages': message})
