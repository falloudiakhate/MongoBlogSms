from django.forms import ModelForm
from .models import *
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

         
class  UserForm(UserCreationForm):
    class Meta:
        model=User
        fields=["username","first_name","last_name","email"]
        

class LoginForm(forms.Form):

  username = forms.CharField(max_length = 30, label ="Username")
  password = forms.CharField(max_length = 30, label = "Password", widget = forms.PasswordInput)
  
  
class PasswordForm(forms.Form):
    
  email = forms.CharField(max_length = 30, label ="Email")
  password = forms.CharField(max_length = 30, label = "Password", widget = forms.PasswordInput)


            
class AuthorForm(forms.ModelForm): 
    class Meta:
        model = Author
        fields = ["telephone","photo", "promo", "genie", "entreprise_actuelle"]  
        

