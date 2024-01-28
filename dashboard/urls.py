from django.urls import path
from .views import *

app_name = "dashboard"
urlpatterns = [
    path("", home),
    path("", home, name="dashboard"),
    path("plan-de-suivi/", PlanDeSuiviView.as_view(), name='plan-de-suivi'),
    path("telereeducation/", videocall, name='telereeducation'),
    path("plan-de-suivi/<str:exercice_id>/<str:seance_id>/", PlanDeSuiviView.as_view(), name='exercice_detail'),
    

]
