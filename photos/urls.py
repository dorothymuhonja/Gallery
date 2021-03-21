from . import views
from django.conf import settings
from . import views
from django.conf.urls.static import static
from django.urls import path



urlpatterns=[
    path('', views.index, name='index'),
    path('location/<str:location>', views.image_location, name='location'),
    path('category/<str:category>', views.search_image, name='category'),
    path('search/', views.search_image, name='search')
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)