from django.contrib import admin


from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth import get_user_model

from .models import Task, NewUser
from .forms import NewUserChangeForm,NewUserCreationForm

class UserAdmin(BaseUserAdmin):
  add_form = NewUserCreationForm
  form = NewUserChangeForm
  model = NewUser
  fieldsets = (
      (None, {'fields': ('username','email', 'password', )}),
      (_('Personal info'), {'fields': ('first_name', 'last_name')}),
      (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'user_permissions')}),
      (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
        (_('user_info'), {'fields': ('phone_no','profile_pic')}),
  )
  add_fieldsets = (
      (None, {
          'classes': ('wide', ),
          'fields': ('email', 'password1', 'password2','is_staff','is_active'),
      }),
  )
  list_display = ['email', 'first_name', 'last_name', 'is_staff', "phone_no"]
  search_fields = ('email', 'first_name', 'last_name')
  ordering = ('email', )

# Register your models here.
admin.site.register(Task)
admin.site.register(NewUser,UserAdmin)
