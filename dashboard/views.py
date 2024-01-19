from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from .models import Exercice, Patient, PlanDeSuivi
# Create your views here.
app_name = "dashboard"
app_path = "dashboard/patient/"


def home(request):
    return render(request, f"{app_path}dashboard.html", locals())



class PlanDeSuiviView(ListView):
    model = PlanDeSuivi
    template_name = f"{app_path}plan_de_suivi.html"
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        patient = Patient.objects.first()
        context["patient"] = patient
        pds = PlanDeSuivi.objects.filter(patient=patient).first()
        context["plan_de_suivi"] = pds
        print(pds)
        exercies = Exercice.objects.filter(plan_de_suivi=pds)
        context["exercises"] = exercies
        print(exercies)
        return context
    

def videocall(request):

    name = "Anonyme"
    return render(request, f"{app_path}video_call.html", {'name':name})


