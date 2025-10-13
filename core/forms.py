from django import forms
from .models import Core

class CoreForm(forms.ModelForm):
    class Meta:
        model = Core
        fields = ['official_name',
                   'number', 
                   'province', 
                   'statut',
                   'promo'

                   ]
     
        widgets = {
            'official_name': forms.TextInput(attrs={'class': 'form-control'}),
            'number': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Numero d\'agrement du Minister de l\'Enseignement Primaire, Secondaire et Technique'}),
            'province': forms.TextInput(attrs={'class': 'form-control'}),
            'promo': forms.TextInput(attrs={'class': 'form-control'}),
        }
