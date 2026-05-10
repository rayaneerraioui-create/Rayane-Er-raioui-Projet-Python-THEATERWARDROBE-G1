from django.urls import path

from . import views


urlpatterns = [

    path(
        '',
        views.listeActeur,
        name='listeActeur'
    ),

    path(
        'ajoutActeur/',
        views.ajoutActeur,
        name='ajoutActeur'
    ),

    path(
        'editActeur/<int:acteur_id>',
        views.editActeur,
        name='editActeur'
    ),

    path(
        'deleteActeur/<int:acteur_id>',
        views.deleteActeur,
        name='deleteActeur'
    ),
]