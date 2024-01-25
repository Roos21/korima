from django.db import models
from django.utils import timezone
from dashboard.managers import CustomUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from hashid_field import HashidField
from django.utils.translation import gettext_lazy as _

# Create your models here.
class CustomUser(AbstractBaseUser, PermissionsMixin):
    reference_id = HashidField(prefix="practitioner_", min_length=20, primary_key=True)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(_("email address"), unique=True)
    first_name = models.CharField(_("first name"), max_length=150)
    last_name = models.CharField(_("first name"), max_length=150)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    is_confirmed = models.BooleanField(default=False)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def get_full_name(self):
        """
        Retourne le nom complet de l'utilisateur (prénom + nom).
        """
        return f"{self.first_name} {self.last_name}"
    
    
    def get_last_login_display(self):
        """
        Retourne une chaîne représentant la durée écoulée depuis la dernière connexion.
        """
        last_login = self.last_login
        now = timezone.now()

        time_difference = now - last_login

        if time_difference.days > 365:
            years = time_difference.days // 365
            return f"{years} {'année' if years == 1 else 'années'}"
        elif time_difference.days > 30:
            months = time_difference.days // 30
            return f"{months} {'mois' if months == 1 else 'mois'}"
        elif time_difference.days > 0:
            return f"{time_difference.days} {'jour' if time_difference.days == 1 else 'jours'}"
        else:
            hours, remainder = divmod(time_difference.seconds, 3600)
            minutes, _ = divmod(remainder, 60)
            return f"{hours} {'heure' if hours == 1 else 'heures'} et {minutes} {'minute' if minutes == 1 else 'minutes'}"