from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager
from app.models import Base, Brigade, Battalion

# Create your models here.
class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("email address"), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    base = models.ForeignKey(Base, on_delete=models.RESTRICT, null=True)
    brigade = models.ForeignKey(Brigade, on_delete=models.RESTRICT, null=True)
    battalion = models.ForeignKey(Battalion, on_delete=models.RESTRICT, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email