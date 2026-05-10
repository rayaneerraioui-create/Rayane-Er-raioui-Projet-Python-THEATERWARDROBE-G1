from django import forms

from .models import Acteur


class GestionActeurs(forms.ModelForm):

    class Meta:

        model = Acteur

        fields = [
            'prenom',
            'nom',
            'mensurations'
        ]

        widgets = {

            'prenom': forms.TextInput(attrs={
                'class': 'form-control'
            }),

            'nom': forms.TextInput(attrs={
                'class': 'form-control'
            }),

            'mensurations': forms.TextInput(attrs={
                'class': 'form-control'
            }),
        }