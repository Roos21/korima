from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

# from phonenumber_field.modelfields import PhoneNumberField


class Genre(models.Model):
    GENRE = (
        ("Masculin", "Masculin"),
        ("Feminin", "Feminin"),
    )
    genre = models.CharField(max_length=50, choices=GENRE)

    def __str__(self) -> str:
        return self.genre


class CustomUser(AbstractUser):
    nom = models.CharField(
        max_length=100, verbose_name="Nom", help_text="Entrez le nom de l'utilisateur"
    )
    prenom = models.CharField(
        max_length=100,
        verbose_name="Prénom",
        help_text="Entrez le prénom de l'utilisateur",
    )
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
    mail = models.EmailField(
        verbose_name="E-mail", help_text="Entrez l'adresse e-mail de l'utilisateur"
    )


class Praticien(CustomUser):
    fonction = models.CharField(
        max_length=100,
        verbose_name="Fonction",
        help_text="Entrez la fonction du praticien",
    )


class Patient(CustomUser):
    date = models.DateTimeField(
        verbose_name="Date", help_text="Entrez la date du patient"
    )


class AntecedantsMedicaux(models.Model):
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
