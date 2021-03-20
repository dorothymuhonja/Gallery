from django.shortcuts import render
from .models import Image, Location


def index(request):
    images = Image.objects.all()
    locations = Location.get_locations()
    return render(request, 'index.html', {'images': images[::-1], 'locations': locations})

def image_location(request, location):
    images = Image.filter_by_location(location)
    return render(request, 'location.html', {'location_images': images})
