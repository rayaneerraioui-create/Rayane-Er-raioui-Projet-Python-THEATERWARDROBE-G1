from django.urls import path

from . import views


urlpatterns = [

    path(
        '',
        views.listeCostume,
        name='listeCostume'
    ),

    path(
        'ajoutCostume/',
        views.ajoutCostume,
        name='ajoutCostume'
    ),

    path(
        'editCostume/<int:costume_id>',
        views.editCostume,
        name='editCostume'
    ),

    path(
        'deleteCostume/<int:costume_id>',
        views.deleteCostume,
        name='deleteCostume'
    ),
]