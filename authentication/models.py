from django.db import models
from django.utils import timezone
from dashboard.managers import CustomUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from hashid_field import HashidField
from django.utils.translation import gettext_lazy as _

# Create your models here.
class CustomUser(AbstractBaseUser, PermissionsMixin):
    reference_id = HashidField(prefix="practitioner_", min_length=20, primary_key=True)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(_("email address"), unique=True)
    first_name = models.CharField(_("first name"), max_length=150)
    last_name = models.CharField(_("first name"), max_length=150)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    objects = CustomUserManager()

    def __str__(self):
        return self.email
