from django.contrib.auth.form import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
  class Meta(UserCreationForm):      # Meta class bo`lishi shart chunki formsga qo`shimcha o`zgaruvchilar qo`shyabmiz
    model = CustomUser     # models da yasagan model dan foydalanammiz 
    fields = ('username', 'firstname', 'lastname', 'email', 'age')   #o`zgaruvchilar userni malumotlarini qo`shish yasash
    
    
class CustomUserChangeForm(UserChangeForm):
  class Meta:           # Meta class bo`lishi shart chunki formsdan malumotlarni o`zgartirayabmiz
    model = CustomUser
    fields = ('username', 'firstname', 'lastname', 'email', 'age')
    
    
