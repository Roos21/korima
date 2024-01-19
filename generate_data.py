import os
import django
from faker import Faker
from django.utils import timezone

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "korima_tech.settings")
django.setup()

from dashboard.models import Genre, CustomUser, Praticien, Patient, AntecedantsMedicaux, PlanDeSuivi, Exercice, Seance, Chat, RendezVous, Equipement, Commande
import pytz
fake = Faker()



# Génération des antécédents médicaux
for _ in range(100):
    patient = Patient.objects.order_by("?").first()
    AntecedantsMedicaux.objects.create(
        libele=fake.word(),
        patient=patient,
        date=fake.date_time_this_decade(tzinfo=pytz.utc),
    )

# Génération des plans de suivi
for _ in range(100):
    PlanDeSuivi.objects.create(
        description=fake.sentence(),
        periode=fake.word(),
    )

# Génération des exercices
for _ in range(100):
    plan_de_suivi = PlanDeSuivi.objects.first()
    Exercice.objects.create(
        titre=fake.word(),
        description=fake.sentence(),
        duree=fake.random_int(min=10, max=60),
        plan_de_suivi=plan_de_suivi,
    )

# Génération des séances
for _ in range(100):
    exercice = Exercice.objects.order_by("?").first()
    Seance.objects.create(
        titre=fake.word(),
        source=fake.word(),
        exercice=exercice,
    )

# Génération des chats
for _ in range(200):
    Chat.objects.create(
        source=fake.word(),
        destinateur=fake.word(),
        message=fake.text(),
    )

# Génération des rendez-vous
for _ in range(100):
    patient = Patient.objects.order_by("?").first()
    praticien = Praticien.objects.order_by("?").first()
    RendezVous.objects.create(
        patient=patient,
        praticien=praticien,
        date=fake.date_time_this_decade(tzinfo=pytz.utc),
        lieu=fake.word(),
        details=fake.sentence(),
    )

# Génération des équipements
for _ in range(100):
    Equipement.objects.create(
        nom=fake.word(),
        type=fake.word(),
        description=fake.sentence(),
        prix=fake.random_int(min=50, max=500),
    )

# Génération des commandes
for _ in range(100):
    equipement = Equipement.objects.order_by("?").first()
    patient = Patient.objects.order_by("?").first()
    Commande.objects.create(
        equipement=equipement,
        patient=patient,
        quantite=fake.random_int(min=1, max=5),
        date=fake.date_time_this_decade(tzinfo=pytz.utc),
    )

print("Données de test générées avec succès!")
