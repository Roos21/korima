from django.urls import path
from .views import *

app_name = "dashboard"
urlpatterns = [
    path("", home),
    path("", home, name="dashboard"),
    path("", home, name="dashboard_praticien"),
    path("plan-de-suivi/", PlanDeSuiviView.as_view(), name='plan-de-suivi'),
    path("telereeducation/", videocall, name='telereeducation'),
    path("chat/", room, name='chat'),
    path("plan-de-suivi/<str:exercice_id>/<str:seance_id>/", PlanDeSuiviView.as_view(), name='exercice_detail'),
    path("plan-de-suivi/<str:exercice_id>/<str:seance_id>/", ValidateSeance.as_view(), name='exercice_detail'),
    path("plan-de-suivi/suivi-progression/", ValidateSeance.as_view(), name='suivi_progression'),
    path("plan-de-suivi/tele-reeducation/", ValidateSeance.as_view(), name='tele_reeducation'),
    path("plan-de-suivi/ask-question/", ValidateSeance.as_view(), name='ask_question'),
    path("condition-d-utilisation/", ConditionUtilisation.as_view(), name = 'condition_d_utilisation'),
    

]
