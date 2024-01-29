from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models
from hashid_field import HashidField
from authentication.models import CustomUser
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.core.validators import MinValueValidator
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.text import slugify

# from phonenumber_field.modelfields import PhoneNumberField

class Room(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

class Message(models.Model):
    reference_id = HashidField(prefix="chat_", min_length=20, primary_key=True)
    room = models.ForeignKey(Room, related_name='messages', on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, related_name='users', on_delete=models.CASCADE)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('date_added',)

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


class Praticien(models.Model):
    reference_id = HashidField(prefix="practitioner_", min_length=20, primary_key=True)
    user_reference = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        default=1,
        related_name="reference_utilisateur",
    )
    fonction = models.CharField(
        max_length=100,
        verbose_name="Fonction",
        help_text="Entrez la fonction du praticien",
    )
    genre = models.ForeignKey(
        Genre, on_delete=models.CASCADE, verbose_name="Genre", default=1
    )
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

class Equipement(models.Model):
    reference_id = HashidField(prefix="product_", min_length=20, primary_key=True)

    nom = models.CharField(
        max_length=100, verbose_name="Nom", help_text="Entrez le nom de l'équipement"
    )
    type = models.CharField(
        max_length=100, verbose_name="Type", help_text="Entrez le type de l'équipement", blank=True
    )
    description = models.TextField(
        max_length=255,
        verbose_name="Description",
        help_text="Entrez la description de l'équipement",
    )
    conseil = models.TextField(
        max_length=255,help_text="Entrez un bref conseil d'une phrase", default='',
    )
    prix = models.FloatField(
        validators=[MinValueValidator(1)],verbose_name="Prix", help_text="Entrez le prix de l'équipement"
    )
    quantite = models.IntegerField(
        validators=[MinValueValidator(1)], verbose_name="Quantité", help_text="Entrez la quantité disponible de l'équipement",default=1,
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
    date = models.DateTimeField(
        verbose_name="Date", help_text="Entrez la date des antécédents médicaux"
    )

class Commande(models.Model):
    reference_id = HashidField(prefix="command_", min_length=20, primary_key=True)

    equipement = models.ForeignKey(
        Equipement, on_delete=models.CASCADE, verbose_name="Équipement"
    )
    quantite = models.IntegerField(
        verbose_name="Quantité", help_text="Entrez la quantité commandée"
    )
    date = models.DateTimeField(
        verbose_name="Date", help_text="Entrez la date de la commande"
    )


class Patient(models.Model):
    reference_id = HashidField(prefix="patient_", min_length=20, primary_key=True)
    user_reference = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        default=1,
        related_name="p_reference_utilisateur",
    )

    date = models.DateTimeField(
        verbose_name="Date", help_text="Entrez la date du patient"
    )
    genre = models.ForeignKey(
        Genre, on_delete=models.CASCADE, verbose_name="Genre", default=1
    )
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
    commandes = models.ManyToManyField(Commande, related_name='patients', blank=True)
    antecedents_medicaux = models.ManyToManyField(AntecedantsMedicaux, related_name='patients_antecedents_medicaux', blank=True)

@receiver(post_save, sender=Patient)
def create_room_for_patient(sender, instance, created, **kwargs):
    if created:
        Room.objects.create(
            name=f"S{instance.user_reference.username}",
            slug=slugify(f"room_{instance.user_reference.username}")
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
    
    patient = models.ForeignKey('Patient', related_name='plans_de_suivi', on_delete=models.CASCADE, default=1)


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
    
    def nb_seances(self):
        return Seance.objects.filter(exercice=self).count()
    def seances(self):
        return Seance.objects.filter(exercice=self)

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
    is_validated = models.BooleanField(default=False)
    comment = models.TextField(max_length=2048, verbose_name="Comment", help_text='Entrez le commentaire de la séance', default='Lorem ipsum, dolor sit amet consectetur adipisicing elit. Quos ut labore rem porro. Totam culpa atque ad! Numquam, deleniti cupiditate est ea, cum repellat saepe animi accusamus aliquid necessitatibus facilis?')

# class Chat(models.Model):
#     reference_id = HashidField(prefix="chat_", min_length=20, primary_key=True)

#     source = models.CharField(
#         max_length=100, verbose_name="Source", help_text="Entrez la source du chat"
#     )
#     destinateur = models.CharField(
#         max_length=100,
#         verbose_name="Destinataire",
#         help_text="Entrez le destinataire du chat",
#     )
#     message = models.TextField(
#         verbose_name="Message", help_text="Entrez le message du chat"
#     )


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
    
    antecedents_medicaux = models.ManyToManyField(AntecedantsMedicaux, related_name='patients', blank=True)
    
    def time_until_rendezvous(self):
        # Récupère la date actuelle
        now = timezone.now()

        # Calcule la différence entre la date du rendez-vous et la date actuelle
        time_until_rendezvous = self.date - now

        # Convertit la différence en jours, heures et minutes
        days = time_until_rendezvous.days
        hours, remainder = divmod(time_until_rendezvous.seconds, 3600)
        minutes, _ = divmod(remainder, 60)

        # Crée une chaîne de caractères descriptive
        if days > 0:
            return f"Dans {days} {'jours' if days > 1 else 'jour'}"
        elif hours > 0:
            return f"Dans {hours} {'heures' if hours > 1 else 'heure'}"
        elif minutes > 0:
            return f"Dans {minutes} {'minutes' if minutes > 1 else 'minute'}"
        else:
            return "C'est maintenant"


class NewsletterSubscriber(models.Model):
    email = models.EmailField(
        unique=True
        )
    subscribed_at = models.DateTimeField(
        auto_now_add=True
        )

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Abonné à la newsletter'
        verbose_name_plural = 'Abonnés à la newsletter'


class ContactUs(models.Model):

    fullname = models.CharField(
        max_length=250, verbose_name="Nom et Prénom", 
    )
    email = models.EmailField(
        verbose_name="Email", 
    )
    sujet = models.CharField(
        max_length=250, verbose_name="Sujet",
    )
    message = models.TextField(
        verbose_name="Message",
    )
    class Meta:
        verbose_name = 'Boite à lettre'
        verbose_name_plural = 'Boite à lettre'

post_save.connect(create_room_for_patient, sender=Patient)



