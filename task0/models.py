from django.db import models

from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
#from django.conf import settings
from .managers import CustomUserManager

#from django.contrib.auth.models import PermissionsMixin
#from datetime import date

class NewUser(AbstractUser):
    username = models.CharField(max_length = 50, blank = True, null = True, unique = True)
    email = models.EmailField(_('email address'), unique = True)
    phone_no = models.CharField(max_length = 10)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
    
    objects = CustomUserManager()
    
    def __str__(self):
    	return self.email

class Task(models.Model):
    number = models.IntegerField(default =0)
    title = models.CharField(max_length=100)
    complete = models.BooleanField(default=False)
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (f"({self.number}) {self.title}")
        