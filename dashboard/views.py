from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.contrib.auth.decorators import login_required
from .models import Exercice, Patient, PlanDeSuivi, RendezVous, Room, Message
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
        context = super().get_context_data(**kwargs)
        patient = Patient.objects.get(user_reference=self.request.user)
        context["patient"] = patient
        pds = PlanDeSuivi.objects.filter(patient=patient).first()
        context["plan_de_suivi"] = pds
        print(pds)
        exercies = Exercice.objects.filter(plan_de_suivi=pds)
        context["exercises"] = exercies
        print(exercies)
        return context
    

def videocall(request):

    name = request.user
    return render(request, f"{app_path}video_call.html", {'name':name})


# @login_required
# def rooms(request):
#     """ Liste des groupe de chat """
#     rooms = Room.objects.all()
#     return render(request, 'room/rooms.html', {'rooms': rooms})

@login_required
def room(request):
    """ Details groupe de chat """
    room_name = Room.objects.get(slug__contains=request.user.username)
    print(room_name.name)
    #rooms = Room.objects.all()    
    messages = Message.objects.filter(room=room_name)[0:30]
    return render(request, f"{app_path}messagerie.html", {'room': room_name, 'messages':messages})


