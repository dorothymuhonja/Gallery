from django.shortcuts import render, request
from django.http import HttpResponse, Http404
from django.core.exceptions import ObjectDoesNotExist

def main(request):
    try:
        images = Image.objects.all()
        category = Category.objects.all()
        location = Location.objects.all()
    except ObjectDoesNotExist:
        raise Http404()
    return render(request,'index.html', {'images':images, 'category':category, 'location':location})
