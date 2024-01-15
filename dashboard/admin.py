from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(Praticien)
class PraticienAdmin(admin.ModelAdmin):
    search_fields = ("fonction__startswith",)
    list_display = ("reference_id", "user_reference", "fonction", "genre")
    fields = ("fonction", "genre", "age", "ville", "quartier", "user_reference")


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    search_fields = ("reference_id__startswith", )
    list_display = ("reference_id", "user_reference", "genre")
    fields = ("date", "genre", "age", "ville", "quartier", "user_reference")

@admin.register(NewsletterSubscriber)
class NewsletterSubscriberAdmin(admin.ModelAdmin):
    list_display = ("email", "subscribed_at")
    search_fields = ("email",)
    readonly_fields = ("subscribed_at",)

@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ("fullname", "email", "sujet")
    search_fields = ("fullname", "email", "sujet")
    fields = ("fullname", "email", "sujet", "message")
@admin.register(AntecedantsMedicaux)
class AntecedantsMedicauxAdmin(admin.ModelAdmin):
    # search_fields = ("f__startswith", )
    list_display = ("reference_id", "libele", "patient")
    #fields = ("date", "genre", "age", "ville", "quartier", "user_reference")
