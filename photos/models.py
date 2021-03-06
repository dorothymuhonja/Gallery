from django.db import models
from django.utils import timezone
from .models import *
from PIL import Image
from cloudinary.models import CloudinaryField

class Category(models.Model):
    name = models.CharField(max_length=15)

    @classmethod
    def get_categories(cls):
        categories = Category.objects.all()
        return categories

    def __str__(self):
        return self.name

    @classmethod
    def update_category(cls, id, value):
        cls.objects.filter(id=id).update(image=value)


    def save_category(self):
        self.save()

    def delete_category(self):
        Category.objects.filter(id = self.pk).delete()



class Location(models.Model):
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name

    @classmethod
    def get_locations(cls):
        locations = Location.objects.all()
        return locations

    def __str__(self):
        return self.name

    @classmethod
    def update_location(cls, id, value):
        cls.objects.filter(id=id).update(image=value)

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()


class Image(models.Model):
    image = CloudinaryField('images', null=True)
    name = models.CharField(max_length=20)
    description = models.TextField()
    posted_by = models.CharField(max_length=50, default='admin')
    date = models.DateTimeField(default=timezone.now)
    category = models.ForeignKey('Category', on_delete = models.CASCADE, null=True)
    location = models.ForeignKey('Location', on_delete = models.CASCADE, null=True)


    @classmethod
    def filter_by_location(cls, location):
        image_location = Image.objects.filter(location__name=location).all()
        return image_location

    @classmethod
    def filter_by_category(cls, category):
        image_category = Image.objects.filter(category__name=category).all()
        return image_category

    @classmethod
    def update_image(cls, id, value):
        cls.objects.filter(id=id).update(image=value)

    @classmethod
    def get_image_by_id(cls, id):
        image = cls.objects.filter(id=id).all()
        return image


    def __str__(self):
        return self.name


    def save_image(self):
        self.save()
 
    def delete_image(self):
        self.delete()


    class Meta:
        ordering = ['date']