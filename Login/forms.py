from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
        labels = {
            'username'  : 'Nome utente',
            'email'     : 'Email',
            'first_name': 'Nome',
            'last_name' : 'Cognome',
            'password1' : 'Password',
            'password2' : 'Ripeti Password'
        }
        widgets = {
            'username'  : forms.TextInput(attrs={'class': 'input-form', 'placeholder':" "}),
            'email'     :forms.EmailInput(attrs={'class': 'input-form', 'placeholder':" "}),
            'first_name': forms.TextInput(attrs={'class': 'input-form', 'placeholder':" "}),
            'last_name' : forms.TextInput(attrs={'class': 'input-form', 'placeholder':" "}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'input-form', 'placeholder': " "})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'input-form', 'placeholder': " "})
