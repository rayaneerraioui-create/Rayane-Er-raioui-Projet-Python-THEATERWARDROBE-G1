import os
import django
import random

from datetime import date


os.environ.setdefault(
    'DJANGO_SETTINGS_MODULE',
    'theaterwardrobe.settings'
)

django.setup()


from acteurs.models import Acteur
from costumes.models import TypeCostume, Costume


# ----------------------------
# ACTEURS
# ----------------------------

acteurs_data = [

    ("Jean", "Dupont", "M"),
    ("Sophie", "Martin", "S"),
    ("Lucas", "Bernard", "L"),
    ("Emma", "Robert", "M"),
    ("Nina", "Petit", "XS"),

]


acteurs = []

for prenom, nom, mensurations in acteurs_data:

    acteur = Acteur.objects.create(

        prenom=prenom,
        nom=nom,
        mensurations=mensurations
    )

    acteurs.append(acteur)


# ----------------------------
# TYPES DE COSTUMES
# ----------------------------

types_data = [

    ("Costume Médiéval", "Moyen Âge"),
    ("Costume Romain", "Antiquité"),
    ("Costume Renaissance", "Renaissance"),
    ("Costume Futuriste", "Futur"),
    ("Costume Traditionnel", "Époque Moderne"),

]


types_costumes = []

for libelle, epoque in types_data:

    type_costume = TypeCostume.objects.create(

        libelle=libelle,
        epoque=epoque
    )

    types_costumes.append(type_costume)


# ----------------------------
# COSTUMES
# ----------------------------

couleurs = [
    "Rouge",
    "Noir",
    "Bleu",
    "Vert",
    "Blanc"
]

tailles = [
    "S",
    "M",
    "L",
    "XL"
]

etats = [
    "Neuf",
    "Bon état",
    "À réparer",
    "Usé"
]


for i in range(15):

    emprunte = random.choice([True, False])

    Costume.objects.create(

        type_costume=random.choice(types_costumes),

        acteur=random.choice(acteurs)
        if emprunte else None,

        couleur=random.choice(couleurs),

        taille=random.choice(tailles),

        etat=random.choice(etats),

        date_emprunt=date.today()
        if emprunte else None
    )


print("Base de données remplie avec succès !")