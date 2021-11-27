from django.shortcuts import render
from django.conf import settings
from django.http import response
from django.http.response import HttpResponse
from users.models import Profile,Address,Education,Experience,Skill,SkillItem
from web.models import Subscribe,Testimonial,Contact
from works.models import Service, Project


# Create your views here.
def index(request):
    profile = Profile.objects.get(user_id=1)
    skills = Skill.objects.filter(user_id=profile.pk)
    skill_items = SkillItem.objects.filter(skill__user_id=profile.pk)
    educations = Education.objects.all()
    experiences = Experience.objects.all()
    services = Service.objects.all()
    projects = Project.objects.all()
    testimonials = Testimonial.objects.all()

    context = {
        "profile" : profile,
        "educations" : educations,
        "experiences" : experiences,
        "services" : services,
        "skills" : skills,
        "skill_items" : skill_items,
        "projects" : projects,
        "testimonials" : testimonials,
    }


    return render(request, "index.html",context = context)

