from django.db import models
from django.db.models.deletion import CASCADE


# Create your models here.
class Testimonial(models.Model):
    client = models.ForeignKey("users.Client",on_delete=models.CASCADE,blank=True,null=True)
    message = models.TextField()

    def __str__(self):
        return self.message



class Contact(models.Model):
    name = models.CharField(max_length=255,null=True,blank=True)
    email = models.EmailField(null=True,blank=True)
    subject = models.CharField(max_length=255,null=True,blank=True)
    message = models.TextField(null=True,blank=True)

    class Meta:
        db_table = "web_contact"
        ordering = ["-id"]

    def __str__(self):
        return self.name


class Subscribe(models.Model):
    email = models.EmailField()

    def __str__(self):
     return self.email