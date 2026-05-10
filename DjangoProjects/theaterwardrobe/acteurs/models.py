from django.db import models


class Acteur(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    mensurations = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.prenom} {self.nom}"