import os
import django
from faker import Faker
from django.utils import timezone
import pytz
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "korima_tech.settings")
django.setup()

from dashboard.models import Genre, CustomUser, Praticien, Patient, AntecedantsMedicaux, PlanDeSuivi, Exercice, Seance, Chat, RendezVous, Equipement, Commande

fake = Faker()
# Génération des utilisateurs
""" for _ in range(10):
    email = fake.email()

    while CustomUser.objects.filter(email=email).exists():
        email = fake.email()

    user = CustomUser(
        username=fake.user_name(),
        email=email,
        first_name=fake.first_name(),
        last_name=fake.last_name(),
        is_staff=fake.boolean(),
        is_active=fake.boolean(),
        date_joined=fake.date_time_this_decade(tzinfo=pytz.utc),  # Utilisation de pytz.utc
    )

    user.save() """
""" """
for _ in range(10): 
    # Génération des praticiens
    Praticien.objects.create(
        user_reference=CustomUser.objects.get(email=fake.random_element(elements=[e.email for e in CustomUser.objects.all()])),
        fonction=fake.job(),
        genre=Genre.objects.get(genre=fake.random_element(elements=["Masculin", "Feminin"])),
        age=fake.random_int(min=25, max=60),
        ville=fake.city(),
        quartier=fake.word(),
    )

    # Génération des patients
    Patient.objects.create(
        user_reference=CustomUser.objects.get(email=fake.random_element(elements=[e.email for e in CustomUser.objects.all()])),
        date=fake.date_time_this_decade(tzinfo=pytz.utc),
        genre=Genre.objects.get(genre=fake.random_element(elements=["Masculin", "Feminin"])),
        age=fake.random_int(min=5, max=90),
        ville=fake.city(),
        quartier=fake.word(),
    )
