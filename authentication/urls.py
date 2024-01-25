from django.urls import path
from .views import LoginView, RegisterView

app_name = 'authentication'  # Assure-toi que cela correspond à l'application de ton projet

urlpatterns = [
    # ... autres URLs de l'application ...
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    # ... autres URLs de l'application ...
]