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
    # search_fields = ("f__startswith", )
    list_display = ("reference_id", "user_reference", "genre")
    fields = ("date", "genre", "age", "ville", "quartier", "user_reference")
