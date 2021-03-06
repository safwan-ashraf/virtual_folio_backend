from django.db import models
from django.db.models.deletion import CASCADE


# Create your models here.
class Service(models.Model):
    image = models.FileField(upload_to="service/")
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Project(models.Model):
    thumbnail = models.ImageField(upload_to="projects/thumbnails/", blank=True, null=True)
    feature_image = models.ImageField(upload_to="projects/feature_image/", blank=True, null=True)
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=255)
    is_completed = models.BooleanField(default=False)
    is_satisfied = models.BooleanField(default=False)
    clients = models.ForeignKey("users.Client",on_delete = models.CASCADE,blank=True,null=True)
    category = models.ForeignKey("works.Category",on_delete = models.CASCADE,blank=True,null=True)
    

    def __str__(self):
        return self.title


class Subscribe(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email