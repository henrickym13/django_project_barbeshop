from django import forms
from . import models

class ServiceForm(forms.ModelForm):

    class Meta:
        model = models.Services
        fields = ['name', 'price']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'name': 'Nome',
            'price': 'Preço',
        }