from django import forms

class PagoForm(forms.Form):
    nombre_tarjeta = forms.CharField(label='Nombre en la tarjeta', required=True)
    numero_tarjeta = forms.CharField(label='Número de tarjeta', required=True)
    codigo = forms.CharField(label='Código de seguridad', required=True)
