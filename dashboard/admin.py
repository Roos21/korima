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

@admin.register(Equipement)
class EquipementAdmin(admin.ModelAdmin):
    list_display = ('nom', 'type', 'prix','quantite')
    search_fields = ['nom', 'type', 'description']
    list_filter = ['type']
    ordering = ['nom']

@admin.register(Commande)
class CommandeAdmin(admin.ModelAdmin):
    list_display = ('equipement', 'patient', 'quantite', 'date')
    search_fields = ['equipement__nom', 'patient__nom']
    list_filter = ['date']
    ordering = ['-date']


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug',)
    search_fields = ('name',)

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('reference_id', 'room', 'user', 'content', 'date_added',)
    search_fields = ('room__name', 'user__username',)    