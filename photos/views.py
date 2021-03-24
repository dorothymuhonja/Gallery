from django.shortcuts import render
from .models import Image, Location, Category


def index(request):
    images = Image.objects.all()
    locations = Location.get_locations()
    categories = Category.get_categories()
    return render(request, 'index.html', {'images': images[::-1], 'locations': locations, 'categories': categories})

def image_location(request, location):
    images = Image.filter_by_location(location)
    return render(request, 'location.html', {'location_images': images})

def image_category(request, category):
    images = Image.filter_by_category(category)
    return render(request, 'category.html', {'category_images': images})



