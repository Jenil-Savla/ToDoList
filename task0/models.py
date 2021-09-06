from django.db import models

from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

from .managers import CustomUserManager

#from django.contrib.auth.models import PermissionsMixin
from django.utils import timezone

class NewUser(AbstractUser):
    username = models.CharField(max_length = 10, blank = True, null = True, unique = True)
    email = models.EmailField(_('email address'), unique = True)
    phone_no = models.CharField(max_length = 10)
    profile_pic = models.ImageField(null = True ,blank=True, default = './media/arcreactor.png')
    
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']
    
    objects = CustomUserManager()
    
    def __str__(self):
    	return self.email

class Task(models.Model):
    number = models.IntegerField(default =0)
    title = models.CharField(max_length=100)
    complete = models.BooleanField(default=False)
    datetime = models.DateTimeField(auto_now_add=True)
    due = models.DateTimeField()
    
    def duechecker(self):
    	if self.due <= timezone.now():
    		self.complete = True
    	else:
    		pass

    def __str__(self):
        return (f"({self.number}) {self.title}")
        