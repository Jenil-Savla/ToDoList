from django import forms
from django.forms import ModelForm
from .models import *

class UserForm(forms.ModelForm):#
	class Meta:
		model = User
		fields = '__all__'
	
class TaskForm(forms.ModelForm):
    title = forms.CharField(max_length = 100)
    class Meta:
        model = Task
        fields = '__all__'