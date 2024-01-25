from django.contrib import admin

# Register your models here.
from authentication.models import CustomUser as User
from .models import Message

#admin.site.register(Room)
admin.site.register(Message)
