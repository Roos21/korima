from django.shortcuts import render
from django.views import View

# Create your views here.

class LoginView(View):
    template_name = 'name.html'
    def get(self, request, *args, **kwargs):
        return render(request, 'login.html', {})

    def post(self, request, *args, **kwargs):
        return render(request, 'login.html', {})