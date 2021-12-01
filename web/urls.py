from django.urls import path
from web.views import index,contact,subscribe



app_name = "web"

urlpatterns = [
    path("", index, name="index"),
    path("contact/", contact, name="contact"),
    path("subscribe/", subscribe, name="subscribe"),
    # path("", category, name="category")
]