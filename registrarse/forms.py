from django import forms  
from django.contrib.auth.models import User  
from django.contrib.auth.forms import UserCreationForm  
from django.core.exceptions import ValidationError  
from django.forms.fields import EmailField  
from django.forms.forms import Form  


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
    
    cui = forms.IntegerField(label='CUI', help_text='Código Único de Identificación CUI')
    profile_imagen = forms.ImageField(label='Foto de perfil', required=False)  # Cambia required a False

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden.")
        
        return password2

    def email_clean(self):
        email = self.cleaned_data.get('email')
        new = User.objects.filter(email=email)

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("El email ya está vinculado con otra cuenta, utiliza uno diferente.")
        return email
    
