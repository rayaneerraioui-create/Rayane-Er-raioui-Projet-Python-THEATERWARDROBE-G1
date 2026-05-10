from django import forms

from .models import Costume


class GestionCostumes(forms.ModelForm):

    class Meta:

        model = Costume

        fields = [
            'type_costume',
            'acteur',
            'couleur',
            'taille',
            'etat',
            'date_emprunt'
        ]

        widgets = {

            'type_costume': forms.Select(attrs={
                'class': 'form-select'
            }),

            'acteur': forms.Select(attrs={
                'class': 'form-select'
            }),

            'couleur': forms.TextInput(attrs={
                'class': 'form-control'
            }),

            'taille': forms.TextInput(attrs={
                'class': 'form-control'
            }),

            'etat': forms.Select(attrs={
                'class': 'form-select'
            }),

            'date_emprunt': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
        }