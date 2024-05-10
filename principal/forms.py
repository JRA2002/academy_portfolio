from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm

class LoginForm(AuthenticationForm):
    pass
class RegisterForm(AuthenticationForm):
    email = forms.EmailField(label='email')
    first_name = forms.CharField(label='first name')
    last_name = forms.CharField(label='last name')

    class Meta():
        model = User
        fields = ['username','email','first_name','last_name','password1','password2']
        
