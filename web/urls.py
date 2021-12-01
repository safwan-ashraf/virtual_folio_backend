from django.urls import path
from web.views import index,contact



app_name = "web"

urlpatterns = [
    path("", index, name="index"),
    path("contact/", contact, name="contact"),
    # path("", category, name="category")
]