from django.urls import path
from .views import *

app_name = "equipement"
urlpatterns = [
    path("",EquipementView.as_view(), name='equipement' ),

]
