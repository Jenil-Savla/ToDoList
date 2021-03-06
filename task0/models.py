from django.db import models

from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

from .managers import CustomUserManager

#from django.contrib.auth.models import PermissionsMixin
from django.utils import timezone

class NewUser(AbstractUser):
    username = models.CharField(max_length = 10, unique = True)
    email = models.EmailField(_('email address'), unique = True)
    phone_no = models.CharField(max_length = 10)
    profile_pic = models.ImageField(blank=True, default = 'arcreactor.png')
    
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']
    
    objects = CustomUserManager()
    
    def __str__(self):
    	return self.email

PRIORITY_CHOICES = ( 

  (1, 'Low'), 

  (2, 'Normal'), 

  (3, 'High'), 

) 


class Task(models.Model):
    user = models.ForeignKey('NewUser', on_delete = models.CASCADE, null = True)
    title = models.CharField(max_length=100)
    complete = models.BooleanField(default=False)
    datetime = models.DateTimeField(auto_now_add=True)
    due = models.DateTimeField()
    priority = models.IntegerField(choices=PRIORITY_CHOICES, default=2)
    
    def duechecker(self):
    	if self.due <= timezone.now():
    		self.title += ' (Past Due) '
    	else:
    		pass
    	
    class Meta:
    	ordering = ['due','-priority']

    def __str__(self):
        return (f"{self.title}")
        