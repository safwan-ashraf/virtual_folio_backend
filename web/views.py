import json
from django.shortcuts import render
from django.conf import settings
from django.http import response
from django.http.response import HttpResponse
from users.models import Profile,Address,Education,Experience,Skill,SkillItem,Client
from web.models import Subscribe,Testimonial,Contact
from works.models import Service, Project, Category
from web.forms import ContactForm,SubscribeForm


# Create your views here.
def index(request):
    category = request.GET.get('category')
    profile = Profile.objects.get(user_id=1)
    skills = Skill.objects.filter(user_id=profile.pk)
    skill_items = SkillItem.objects.filter(skill__user_id=profile.pk)
    clients = Client.objects.all()
    no_of_clients = Client.objects.all().count()
    completed_count = Project.objects.filter(is_completed=True).count()
    pending_count = Project.objects.filter(is_completed=False).count()
    satisfied_count = Project.objects.filter(is_satisfied=True).count()
    educations = Education.objects.all()
    experiences = Experience.objects.all()
    services = Service.objects.all()[:4]
    categories = Category.objects.all()
    testimonials = Testimonial.objects.all()[:1]
    form_c = ContactForm()
    form_s = SubscribeForm()

    if category:
        if Project.objects.filter(category__name=category).exists():
            projects = Project.objects.filter(category__name=category)[:6]
        else:
           projects = Project.objects.all()[:6] 
    else:
        projects = Project.objects.all()[:6]

    context = {
        "profile" : profile,
        "educations" : educations,
        "experiences" : experiences,
        "services" : services,
        "skills" : skills,
        "skill_items" : skill_items,
        "projects" : projects,
        "testimonials" : testimonials,
        "clients" : clients,
        "no_of_clients" : no_of_clients,
        "completed_count" : completed_count,
        "pending_count" : pending_count,
        "satisfied_count" : satisfied_count,
        "categories" : categories,
        "category" : category,
        "form_c": form_c,
        "form_s": form_s
    }


    return render(request, "index.html",context = context)


def contact(request):
    form = ContactForm(request.POST)
    email = request.POST.get("email")
    if form.is_valid():
        if not Contact.objects.filter(email=email).exists():
            form.save()
            response_data = {
                "status" : "success",
                "title" : "Successfully registered",
                "message" : "You subscribed to our newsletter successfully."
            }
        else:
            response_data = {
            "status" : "error",
            "title" : "You are already subscribed",
            "message" : "Already subscribed"
        }
    else:
        response_data = {
            "status" : "error",
            "title" : "You are already subscribed",
            "message" : "Already subscribed"
        }
    
    return HttpResponse(json.dumps(response_data),content_type="application/javascript")


def subscribe(request):
    form = SubscribeForm(request.POST)
    email = request.POST.get("email")
    if form.is_valid():
        if not Subscribe.objects.filter(email=email).exists():
            form.save()
            response_data = {
                "status" : "success",
                "title" : "Successfully registered",
                "message" : "You subscribed to our newsletter successfully."
            }
        else:
            response_data = {
            "status" : "error",
            "title" : "You are already subscribed",
            "message" : "Already subscribed"
        }
    else:
        response_data = {
            "status" : "error",
            "title" : "You are already subscribed",
            "message" : "Already subscribed"
        }
    
    return HttpResponse(json.dumps(response_data),content_type="application/javascript")
