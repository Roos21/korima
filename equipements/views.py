from typing import Any
from django.shortcuts import render
from dashboard.models import Equipement
from django.views.generic import ListView, DetailView

# Create your views here.

app_path = "equipment/"

class EquipementView(ListView):
    template_name = f"{app_path}equipment.html"
    model = Equipement

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context["equipements"] = Equipement.objects.all()
        return context
