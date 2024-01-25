from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Message
from dashboard.models import Chat,Praticien
from django.shortcuts import get_object_or_404


# Create your views here.
app_name = "dashboard"
app_path = "dashboard/patient/"

#@method_decorator(login_required, name='dispatch')
class ChatRoomView(TemplateView):
    template_name = f"{app_path}messagerie.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_1'] = self.request.user
        context['user_2'] = get_object_or_404(Praticien, fonction="Research scientist (physical sciences)")
        print("User 1:", context['user_1'])
        print("User 2:", context['user_2'])
        return context




