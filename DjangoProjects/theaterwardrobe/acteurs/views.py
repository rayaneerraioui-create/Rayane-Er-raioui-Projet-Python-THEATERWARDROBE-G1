from django.shortcuts import render, redirect

from .models import Acteur

from .forms import GestionActeurs


def listeActeur(request):

    acteurs = Acteur.objects.all()

    context = {
        "acteurs": acteurs
    }

    return render(
        request,
        'acteurs/listeActeur.html',
        context
    )


def ajoutActeur(request):

    form = GestionActeurs(
        request.POST or None
    )

    if form.is_valid():

        form.save()

        return redirect('listeActeur')

    context = {
        "form": form
    }

    return render(
        request,
        'acteurs/ajoutActeur.html',
        context
    )


def editActeur(request, acteur_id):

    acteur = Acteur.objects.get(
        id=acteur_id
    )

    form = GestionActeurs(
        request.POST or None,
        instance=acteur
    )

    if form.is_valid():

        form.save()

        return redirect('listeActeur')

    context = {
        "form": form
    }

    return render(
        request,
        'acteurs/editActeur.html',
        context
    )


def deleteActeur(request, acteur_id):

    acteur = Acteur.objects.get(
        id=acteur_id
    )

    acteur.delete()

    return redirect('listeActeur')