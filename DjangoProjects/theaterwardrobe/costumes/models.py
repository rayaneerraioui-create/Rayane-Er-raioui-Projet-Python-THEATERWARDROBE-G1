from django.db import models
from acteurs.models import Acteur


class TypeCostume(models.Model):
    libelle = models.CharField(max_length=100)
    epoque = models.CharField(max_length=100)

    def __str__(self):
        return self.libelle


class Costume(models.Model):

    ETAT_CHOICES = [
        ('Neuf', 'Neuf'),
        ('Bon état', 'Bon état'),
        ('À réparer', 'À réparer'),
        ('Usé', 'Usé'),
    ]

    type_costume = models.ForeignKey(
        TypeCostume,
        on_delete=models.CASCADE
    )

    acteur = models.ForeignKey(
        Acteur,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    couleur = models.CharField(max_length=50)

    taille = models.CharField(max_length=10)

    etat = models.CharField(
        max_length=20,
        choices=ETAT_CHOICES
    )

    date_emprunt = models.DateField(
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.type_costume} - {self.couleur}"