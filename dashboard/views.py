from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView
from django.contrib.auth.decorators import login_required
from .models import Exercice, Patient, PlanDeSuivi, RendezVous, Seance
from django.utils import timezone
# Create your views here.
app_name = "dashboard"
app_path = "dashboard/patient/"

def get_patient_from_user(user_instance):
    try:
        # Vérifie si l'utilisateur est un patient
        patient_instance = Patient.objects.get(user_reference=user_instance)
        return patient_instance
    except Patient.DoesNotExist:
        # Si l'utilisateur n'est pas un patient, renvoie None
        return None
@login_required(login_url='/authentication/login')
def home(request):
    now = timezone.now()
    try:
        patient = Patient.objects.get(user_reference=request.user)
        patient_rendezvous = RendezVous.objects.filter(patient=patient, date__gt=now).order_by('date')
        pds = PlanDeSuivi.objects.filter(patient=patient).order_by('-reference_id')
        antecedents_medicaux = patient.antecedents_medicaux.all()
        equipements_commandes = patient.commandes.all()
        if len(pds) >= 5:
            pds = pds[:2]
    except:
        pass  
    return render(request, f"{app_path}dashboard.html", locals())


class PlanDeSuiviView(ListView):
    model = PlanDeSuivi
    template_name = f"{app_path}plan_de_suivi.html"
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        patient = Patient.objects.get(user_reference=self.request.user)
        pds = PlanDeSuivi.objects.filter(patient=patient).first()
        exercice = Exercice.objects.filter(plan_de_suivi=pds).last()
        #exercice = get_object_or_404(Exercice, reference_id=exercie.reference_id)
        seance_actuelle = exercice.seances().filter(is_validated=True).last()
        seance_precedente = None
        if seance_actuelle:
            seance_precedente = exercice.seances().filter(reference_id__lt=seance_actuelle.reference_id).last()

        # Récupérer la séance suivante
        seance_suivante = exercice.seances().filter(reference_id__gt=seance_actuelle.reference_id).first()
        seances = exercice.seances()
        context = super().get_context_data(**kwargs)
        context["patient"] = patient
        context["plan_de_suivi"] = pds
        context["exercice"] = exercice
        context['seance_actuelle'] = seance_actuelle
        context['seance_precedente'] = seance_precedente
        context['seance_suivante'] = seance_suivante
        context['seances'] = seances
        
        for seance in seances:
            print(seance.is_validated)
        return context
    

class ValidateSeance(ListView):
    model = PlanDeSuivi
    template_name = f"{app_path}plan_de_suivi.html"
    def get(self, request, *args, **kwargs):
        seance_actuelle = None
        seance_precedente = None
        exercice = get_object_or_404(Exercice, reference_id=exercice_id)
        seance = get_object_or_404(Seance, reference_id=seance_id)
        seances = exercice.seances()
        if seance is not None:
            seance.valider_seance()
            seance_actuelle = exercice.seances().filter(is_validated=True).last()
            seance_precedente = exercice.seances().filter(reference_id__lt=seance_actuelle.reference_id).last()

        
        seance_suivante = exercice.seances().filter(reference_id__gt=seance_actuelle.reference_id).first()
        seances = exercice.seances()
        return render(request, self.template_name, locals())

    

def videocall(request):

    name = "Anonyme"
    return render(request, f"{app_path}video_call.html", {'name':name})


