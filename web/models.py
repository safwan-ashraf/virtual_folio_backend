from django.db import models


# Create your models here.
class Testimonial(models.Model):
    message = models.TextField()

    def __str__(self):
        return self.id



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