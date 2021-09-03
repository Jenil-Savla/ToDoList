from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Task,NewUser

class NewUserChangeForm(UserChangeForm):
	class Meta:
		model = NewUser
		fields = 'email',
		
class NewUserCreationForm(UserCreationForm):
	class Meta:
		model = NewUser
		fields = 'email',

class TaskForm(forms.ModelForm):
    title = forms.CharField(max_length = 100)
    class Meta:
        model = Task
        fields = '__all__'