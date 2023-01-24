from .models import User
from django.forms import ModelForm

class FUser(ModelForm):
    class Meta:
        model=User
        fields='__all__'
