from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext as _

# Create your models here.

class MyUser(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
