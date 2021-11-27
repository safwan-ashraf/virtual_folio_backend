from django.db import models
from django.db.models.deletion import CASCADE


# Create your models here.
PROFILE_GENDER = (
    ("male","Male"),
    ("female","Female"),
    ("other","Other")
)


class Profile(models.Model):
    user_id = models.AutoField(unique=True, primary_key=True)
    image = models.ImageField(upload_to="profile/")
    name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    address = models.ForeignKey("users.Address",on_delete = models.CASCADE,blank=True,null=True)
    description = models.TextField()
    age = models.IntegerField(blank=True,null=True)
    gender = models.TextField(choices=PROFILE_GENDER)
    resume = models.FileField(upload_to="profile/")

    def __str__(self):
        return self.name


class Address(models.Model):
    district = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    area = models.CharField(max_length=255)
    current_district = models.CharField(max_length=255)
    current_state = models.CharField(max_length=255)
    current_area = models.CharField(max_length=255)

    def __str__(self):
        return self.district
        

class Education(models.Model):
    year = models.IntegerField()
    course = models.CharField(max_length=255)
    university = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.course


class Experience(models.Model):
    year = models.IntegerField()
    company = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    description = models.TextField()
    is_current = models.BooleanField(default=False)

    def __str__(self):
        return self.company


class Skill(models.Model):
    name = models.CharField(max_length=255)
    user_id = models.ForeignKey("users.Profile",on_delete = models.CASCADE,blank=True,null=True)

    def __str__(self):
        return self.name


class SkillItem(models.Model):
    skill = models.ForeignKey("users.Skill",on_delete = models.CASCADE,blank=True,null=True)
    rating = models.IntegerField()
    item = models.CharField(max_length=128)

    def __str__(self):
        return self.item


class Clients(models.Model):
    name =  models.CharField(max_length=255)
    image = models.FileField(upload_to="service/")
    designation = models.CharField(max_length=255)

    def __str__(self):
        return self.name
