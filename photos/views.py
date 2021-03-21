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


def search_image(request):
    if 'imagesearch' in request.GET and request.GET['imagesearch']:
        category = request.GET.get('imagesearch')
        searched_images = Image.search_by_category(category)
        message = f'{category}'
        return render(request, 'search_image.html', {'message': message, "image": searched_images})

    else:
        message = "You haven't searched for any images"
        return render(request, 'search_image.html', {'messages': message})
