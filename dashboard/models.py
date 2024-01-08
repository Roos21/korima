from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models
from hashid_field import HashidField
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone

# from phonenumber_field.modelfields import PhoneNumberField


class Genre(models.Model):
    GENRE = (
        ("Masculin", "Masculin"),
        ("Feminin", "Feminin"),
    )
    genre = models.CharField(max_length=50, choices=GENRE)
    # Including the type of id in the id itself:
    reference_id = HashidField(prefix="gender_", min_length=20, primary_key=True)

    def __str__(self) -> str:
        return self.genre


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("email address"), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, verbose_name="Genre")
    age = models.IntegerField(
        verbose_name="Âge", help_text="Entrez l'âge de l'utilisateur", null=True
    )
    ville = models.CharField(
        max_length=100,
        verbose_name="Ville",
        help_text="Entrez la ville de l'utilisateur",
    )
    quartier = models.CharField(
        max_length=100,
        verbose_name="Quartier",
        help_text="Entrez le quartier de l'utilisateur",
    )
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class Praticien(CustomUser):
    reference_id = HashidField(prefix="practitioner_", min_length=20, primary_key=True)
    fonction = models.CharField(
        max_length=100,
        verbose_name="Fonction",
        help_text="Entrez la fonction du praticien",
    )


class Patient(CustomUser):
    reference_id = HashidField(prefix="patient_", min_length=20, primary_key=True)
    date = models.DateTimeField(
        verbose_name="Date", help_text="Entrez la date du patient"
    )


class AntecedantsMedicaux(models.Model):
    reference_id = HashidField(
        prefix="medical_antecedents_", min_length=20, primary_key=True
    )
    libele = models.CharField(
        max_length=100,
        verbose_name="Libellé",
        help_text="Entrez le libellé des antécédents médicaux",
    )
    patient = models.ForeignKey(
        Patient, on_delete=models.CASCADE, verbose_name="Patient"
    )
    date = models.DateTimeField(
        verbose_name="Date", help_text="Entrez la date des antécédents médicaux"
    )


class PlanDeSuivi(models.Model):
    reference_id = HashidField(
        prefix="follow-up_plan_", min_length=20, primary_key=True
    )
    description = models.CharField(
        max_length=200,
        verbose_name="Description",
        help_text="Entrez la description du plan de suivi",
    )
    periode = models.CharField(
        max_length=100,
        verbose_name="Période",
        help_text="Entrez la période du plan de suivi",
    )


class Exercice(models.Model):
    reference_id = HashidField(prefix="exercise_", min_length=20, primary_key=True)

    titre = models.CharField(
        max_length=100, verbose_name="Titre", help_text="Entrez le titre de l'exercice"
    )
    description = models.CharField(
        max_length=200,
        verbose_name="Description",
        help_text="Entrez la description de l'exercice",
    )
    duree = models.IntegerField(
        verbose_name="Durée", help_text="Entrez la durée de l'exercice"
    )
    plan_de_suivi = models.ForeignKey(
        PlanDeSuivi, on_delete=models.CASCADE, verbose_name="Plan de suivi"
    )


class Seance(models.Model):
    reference_id = HashidField(prefix="session_", min_length=20, primary_key=True)

    titre = models.CharField(
        max_length=100, verbose_name="Titre", help_text="Entrez le titre de la séance"
    )
    source = models.CharField(
        max_length=100, verbose_name="Source", help_text="Entrez la source de la séance"
    )
    exercice = models.ForeignKey(
        Exercice, on_delete=models.CASCADE, verbose_name="Exercice"
    )


class Chat(models.Model):
    reference_id = HashidField(prefix="chat_", min_length=20, primary_key=True)

    source = models.CharField(
        max_length=100, verbose_name="Source", help_text="Entrez la source du chat"
    )
    destinateur = models.CharField(
        max_length=100,
        verbose_name="Destinataire",
        help_text="Entrez le destinataire du chat",
    )
    message = models.TextField(
        verbose_name="Message", help_text="Entrez le message du chat"
    )


class RendezVous(models.Model):
    reference_id = HashidField(prefix="appointment_", min_length=20, primary_key=True)

    patient = models.ForeignKey(
        Patient,
        related_name="patient_rdv",
        on_delete=models.CASCADE,
        verbose_name="Patient",
    )
    praticien = models.ForeignKey(
        Praticien,
        related_name="praticien_rdv",
        on_delete=models.CASCADE,
        verbose_name="Praticien",
    )
    date = models.DateTimeField(
        verbose_name="Date", help_text="Entrez la date du rendez-vous"
    )
    lieu = models.CharField(
        max_length=100, verbose_name="Lieu", help_text="Entrez le lieu du rendez-vous"
    )
    details = models.CharField(
        max_length=200,
        verbose_name="Détails",
        help_text="Entrez les détails du rendez-vous",
    )


class Equipement(models.Model):
    reference_id = HashidField(prefix="product_", min_length=20, primary_key=True)

    nom = models.CharField(
        max_length=100, verbose_name="Nom", help_text="Entrez le nom de l'équipement"
    )
    type = models.CharField(
        max_length=100, verbose_name="Type", help_text="Entrez le type de l'équipement"
    )
    description = models.CharField(
        max_length=200,
        verbose_name="Description",
        help_text="Entrez la description de l'équipement",
    )
    prix = models.FloatField(
        verbose_name="Prix", help_text="Entrez le prix de l'équipement"
    )


class Commande(models.Model):
    reference_id = HashidField(prefix="command_", min_length=20, primary_key=True)

    equipement = models.ForeignKey(
        Equipement, on_delete=models.CASCADE, verbose_name="Équipement"
    )
    patient = models.ForeignKey(
        Patient, on_delete=models.CASCADE, verbose_name="Patient"
    )
    quantite = models.IntegerField(
        verbose_name="Quantité", help_text="Entrez la quantité commandée"
    )
    date = models.DateTimeField(
        verbose_name="Date", help_text="Entrez la date de la commande"
    )
