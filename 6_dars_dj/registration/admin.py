from django.contrib import admin
from .models import Reclama, CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.adim import UserAdmin

class CustomUserAdmin(UserAdmin):
  add_forms = CustomUserCreationForm
  form = CustomUserChangeForm
  model = CustomUser
  list_display = ['username', 'firstname', 'lastname', 'email', 'age', 'is_steff']
  fieldsets = UserAdmin.fieldsets + (
    (None, {'fields': ('age',)}),
  )
  
admin.site.register(Reclama, CustomUserAdmin, CustomUser)
