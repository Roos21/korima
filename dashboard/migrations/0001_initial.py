# Generated by Django 5.0.1 on 2024-01-09 08:23

import django.core.validators
import django.db.models.deletion
import hashid_field.field
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Chat",
            fields=[
                (
                    "reference_id",
                    hashid_field.field.HashidField(
                        alphabet="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890",
                        min_length=20,
                        prefix="chat_",
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "source",
                    models.CharField(
                        help_text="Entrez la source du chat",
                        max_length=100,
                        verbose_name="Source",
                    ),
                ),
                (
                    "destinateur",
                    models.CharField(
                        help_text="Entrez le destinataire du chat",
                        max_length=100,
                        verbose_name="Destinataire",
                    ),
                ),
                (
                    "message",
                    models.TextField(
                        help_text="Entrez le message du chat", verbose_name="Message"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ContactUs",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "fullname",
                    models.CharField(max_length=250, verbose_name="Nom et Prénom"),
                ),
                ("email", models.EmailField(max_length=254, verbose_name="Email")),
                ("sujet", models.CharField(max_length=250, verbose_name="Sujet")),
                ("message", models.TextField(verbose_name="Message")),
            ],
            options={
                "verbose_name": "Boite à lettre",
                "verbose_name_plural": "Boite à lettre",
            },
        ),
        migrations.CreateModel(
            name="Equipement",
            fields=[
                (
                    "reference_id",
                    hashid_field.field.HashidField(
                        alphabet="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890",
                        min_length=20,
                        prefix="product_",
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "nom",
                    models.CharField(
                        help_text="Entrez le nom de l'équipement",
                        max_length=100,
                        verbose_name="Nom",
                    ),
                ),
                (
                    "type",
                    models.CharField(
                        blank=True,
                        help_text="Entrez le type de l'équipement",
                        max_length=100,
                        verbose_name="Type",
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        help_text="Entrez la description de l'équipement",
                        max_length=255,
                        verbose_name="Description",
                    ),
                ),
                (
                    "conseil",
                    models.TextField(
                        default="",
                        help_text="Entrez un bref conseil d'une phrase",
                        max_length=255,
                    ),
                ),
                (
                    "prix",
                    models.FloatField(
                        help_text="Entrez le prix de l'équipement",
                        validators=[django.core.validators.MinValueValidator(1)],
                        verbose_name="Prix",
                    ),
                ),
                (
                    "quantite",
                    models.IntegerField(
                        default=1,
                        help_text="Entrez la quantité disponible de l'équipement",
                        validators=[django.core.validators.MinValueValidator(1)],
                        verbose_name="Quantité",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Genre",
            fields=[
                (
                    "genre",
                    models.CharField(
                        choices=[("Masculin", "Masculin"), ("Feminin", "Feminin")],
                        max_length=50,
                    ),
                ),
                (
                    "reference_id",
                    hashid_field.field.HashidField(
                        alphabet="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890",
                        min_length=20,
                        prefix="gender_",
                        primary_key=True,
                        serialize=False,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="NewsletterSubscriber",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("subscribed_at", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "verbose_name": "Abonné à la newsletter",
                "verbose_name_plural": "Abonnés à la newsletter",
            },
        ),
        migrations.CreateModel(
            name="Patient",
            fields=[
                (
                    "reference_id",
                    hashid_field.field.HashidField(
                        alphabet="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890",
                        min_length=20,
                        prefix="patient_",
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "date",
                    models.DateTimeField(
                        help_text="Entrez la date du patient", verbose_name="Date"
                    ),
                ),
                (
                    "age",
                    models.IntegerField(
                        help_text="Entrez l'âge de l'utilisateur",
                        null=True,
                        verbose_name="Âge",
                    ),
                ),
                (
                    "ville",
                    models.CharField(
                        help_text="Entrez la ville de l'utilisateur",
                        max_length=100,
                        verbose_name="Ville",
                    ),
                ),
                (
                    "quartier",
                    models.CharField(
                        help_text="Entrez le quartier de l'utilisateur",
                        max_length=100,
                        verbose_name="Quartier",
                    ),
                ),
                (
                    "genre",
                    models.ForeignKey(
                        default=1,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="dashboard.genre",
                        verbose_name="Genre",
                    ),
                ),
                (
                    "user_reference",
                    models.ForeignKey(
                        default=1,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="p_reference_utilisateur",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Commande",
            fields=[
                (
                    "reference_id",
                    hashid_field.field.HashidField(
                        alphabet="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890",
                        min_length=20,
                        prefix="command_",
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "quantite",
                    models.IntegerField(
                        help_text="Entrez la quantité commandée",
                        verbose_name="Quantité",
                    ),
                ),
                (
                    "date",
                    models.DateTimeField(
                        help_text="Entrez la date de la commande", verbose_name="Date"
                    ),
                ),
                (
                    "equipement",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="dashboard.equipement",
                        verbose_name="Équipement",
                    ),
                ),
                (
                    "patient",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="dashboard.patient",
                        verbose_name="Patient",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="AntecedantsMedicaux",
            fields=[
                (
                    "reference_id",
                    hashid_field.field.HashidField(
                        alphabet="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890",
                        min_length=20,
                        prefix="medical_antecedents_",
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "libele",
                    models.CharField(
                        help_text="Entrez le libellé des antécédents médicaux",
                        max_length=100,
                        verbose_name="Libellé",
                    ),
                ),
                (
                    "date",
                    models.DateTimeField(
                        help_text="Entrez la date des antécédents médicaux",
                        verbose_name="Date",
                    ),
                ),
                (
                    "patient",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="dashboard.patient",
                        verbose_name="Patient",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="PlanDeSuivi",
            fields=[
                (
                    "reference_id",
                    hashid_field.field.HashidField(
                        alphabet="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890",
                        min_length=20,
                        prefix="follow-up_plan_",
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "description",
                    models.CharField(
                        help_text="Entrez la description du plan de suivi",
                        max_length=200,
                        verbose_name="Description",
                    ),
                ),
                (
                    "periode",
                    models.CharField(
                        help_text="Entrez la période du plan de suivi",
                        max_length=100,
                        verbose_name="Période",
                    ),
                ),
                (
                    "patient",
                    models.ForeignKey(
                        default=1,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="plans_de_suivi",
                        to="dashboard.patient",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Exercice",
            fields=[
                (
                    "reference_id",
                    hashid_field.field.HashidField(
                        alphabet="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890",
                        min_length=20,
                        prefix="exercise_",
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "titre",
                    models.CharField(
                        help_text="Entrez le titre de l'exercice",
                        max_length=100,
                        verbose_name="Titre",
                    ),
                ),
                (
                    "description",
                    models.CharField(
                        help_text="Entrez la description de l'exercice",
                        max_length=200,
                        verbose_name="Description",
                    ),
                ),
                (
                    "duree",
                    models.IntegerField(
                        help_text="Entrez la durée de l'exercice", verbose_name="Durée"
                    ),
                ),
                (
                    "plan_de_suivi",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="dashboard.plandesuivi",
                        verbose_name="Plan de suivi",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Praticien",
            fields=[
                (
                    "reference_id",
                    hashid_field.field.HashidField(
                        alphabet="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890",
                        min_length=20,
                        prefix="practitioner_",
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "fonction",
                    models.CharField(
                        help_text="Entrez la fonction du praticien",
                        max_length=100,
                        verbose_name="Fonction",
                    ),
                ),
                (
                    "age",
                    models.IntegerField(
                        help_text="Entrez l'âge de l'utilisateur",
                        null=True,
                        verbose_name="Âge",
                    ),
                ),
                (
                    "ville",
                    models.CharField(
                        help_text="Entrez la ville de l'utilisateur",
                        max_length=100,
                        verbose_name="Ville",
                    ),
                ),
                (
                    "quartier",
                    models.CharField(
                        help_text="Entrez le quartier de l'utilisateur",
                        max_length=100,
                        verbose_name="Quartier",
                    ),
                ),
                (
                    "genre",
                    models.ForeignKey(
                        default=1,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="dashboard.genre",
                        verbose_name="Genre",
                    ),
                ),
                (
                    "user_reference",
                    models.ForeignKey(
                        default=1,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="reference_utilisateur",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="RendezVous",
            fields=[
                (
                    "reference_id",
                    hashid_field.field.HashidField(
                        alphabet="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890",
                        min_length=20,
                        prefix="appointment_",
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "date",
                    models.DateTimeField(
                        help_text="Entrez la date du rendez-vous", verbose_name="Date"
                    ),
                ),
                (
                    "lieu",
                    models.CharField(
                        help_text="Entrez le lieu du rendez-vous",
                        max_length=100,
                        verbose_name="Lieu",
                    ),
                ),
                (
                    "details",
                    models.CharField(
                        help_text="Entrez les détails du rendez-vous",
                        max_length=200,
                        verbose_name="Détails",
                    ),
                ),
                (
                    "patient",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="patient_rdv",
                        to="dashboard.patient",
                        verbose_name="Patient",
                    ),
                ),
                (
                    "praticien",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="praticien_rdv",
                        to="dashboard.praticien",
                        verbose_name="Praticien",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Seance",
            fields=[
                (
                    "reference_id",
                    hashid_field.field.HashidField(
                        alphabet="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890",
                        min_length=20,
                        prefix="session_",
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "titre",
                    models.CharField(
                        help_text="Entrez le titre de la séance",
                        max_length=100,
                        verbose_name="Titre",
                    ),
                ),
                (
                    "source",
                    models.CharField(
                        help_text="Entrez la source de la séance",
                        max_length=100,
                        verbose_name="Source",
                    ),
                ),
                (
                    "exercice",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="dashboard.exercice",
                        verbose_name="Exercice",
                    ),
                ),
            ],
        ),
    ]
