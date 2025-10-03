from django import forms
from .models import Country

# Formulario basado en el modelo Country
class CountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = ['name', 'abbrev', 'status']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'abbrev': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
