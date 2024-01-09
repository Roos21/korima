from django.urls import path
from .views import home

app_name = "dashboard"
urlpatterns = [
    path("", home),
    path("dashboard/", home),
]
