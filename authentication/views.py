from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login
from django import forms
from .models import CustomUser  # Assure-toi d'importer correctement ton modèle CustomUser

# Create your views here.
class LoginView(View):
    template_name = 'connexion.html'

    def get(self, request):
        # Affiche le formulaire de connexion en cas de requête GET
        return render(request, self.template_name)

    def post(self, request):
        # Gère la soumission du formulaire de connexion en cas de requête POST
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Valide les champs (ajoute des vérifications supplémentaires si nécessaire)
        if not username or not password:
            # Gère les cas où les champs ne sont pas renseignés
            return render(request, self.template_name, {'error_message': 'Veuillez renseigner tous les champs.'})

        # Authentifie l'utilisateur
        user = authenticate(request, username=username, password=password)

        if user is not None:
            if user.is_confirmed == False:
                return render(request, self.template_name, {'error_message': 'Vous ne pouvez pas vous connecter, votre compte est inactif pour le moment'})
            login(request, user)
            # Redirige vers la page souhaitée après la connexion réussie
            return redirect('dashboard:dashboard')  # Remplace 'dashboard:dashboard_home' par l'URL de ta page d'accueil

        # En cas d'échec de connexion, réaffiche le formulaire avec un message d'erreur
        return render(request, self.template_name, {'error_message': 'Nom d\'utilisateur ou mot de passe incorrect.'})

class RegisterView(View):
    template_name = 'inscription.html'

    def get(self, request):
        # Affiche le formulaire d'inscription en cas de requête GET
        return render(request, self.template_name)

    def post(self, request):
        # Gère la soumission du formulaire d'inscription en cas de requête POST
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        repassword = request.POST.get('repassword')

        # Valide les champs (ajoute des vérifications supplémentaires si nécessaire)
        if not username or not email or not password:
            # Gère les cas où les champs ne sont pas renseignés
            return render(request, self.template_name, {'error_message': 'Veuillez renseigner tous les champs.', 'username':username, 'email':email})
        if password != repassword:
            return render(request, self.template_name, {'error_message': 'Les deux mot de passes ne sont pas identifique', 'username':username, 'email':email})
        
        if len(password) < 8:
            return render(request, self.template_name, {'error_message': 'Le mot de passe doit comporter au moins 8 caractères...', 'username':username, 'email':email})
        display_password = f"{password[:2]}{'*' * (len(password) - 4)}{password[-2:]}"        
        user = CustomUser.objects.create_user(username=username, email=email, password=password,is_active=False)
        is_regitred = True
        # Redirige vers la page souhaitée après l'inscription réussie
        return render(request, self.template_name, {'is_regitred': is_regitred, 'username':username, 'password':display_password})
