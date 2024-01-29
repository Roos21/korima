from django.urls import path
from .views import *

app_name = "dashboard"
urlpatterns = [
    path("", home),
    path("", home, name="dashboard"),
    path("plan-de-suivi/", PlanDeSuiviView.as_view(), name='plan-de-suivi'),
    path("telereeducation/", videocall, name='telereeducation'),
    path("chat/", room, name='chat'),

]
