from django.urls import path
from web.views import index,contact,subscribe,category



app_name = "web"

urlpatterns = [
    path("", index, name="index"),
    path("contact/", contact, name="contact"),
    path("subscribe/", subscribe, name="subscribe"),
    path("category/",category, name="category"),
    # path("", category, name="category")
]