from django.shortcuts import render, redirect

from .models import Costume

from .forms import GestionCostumes


def listeCostume(request):

    costumes = Costume.objects.all()

    recherche = request.GET.get('recherche')

    couleur = request.GET.get('couleur')

    taille = request.GET.get('taille')

    date_emprunt = request.GET.get('date_emprunt')

    disponibilite = request.GET.get('disponibilite')

    if recherche:

        costumes = costumes.filter(
            type_costume__libelle__icontains=recherche
        )

    if couleur:

        costumes = costumes.filter(
            couleur__icontains=couleur
        )

    if taille:

        costumes = costumes.filter(
            taille__icontains=taille
        )

    if date_emprunt:

        costumes = costumes.filter(
            date_emprunt=date_emprunt
        )

    if disponibilite == "disponible":

        costumes = costumes.filter(
            acteur__isnull=True
        )

    elif disponibilite == "emprunte":

        costumes = costumes.filter(
            acteur__isnull=False
        )

    context = {
        "costumes": costumes
    }

    return render(
        request,
        'costumes/listeCostume.html',
        context
    )


def ajoutCostume(request):

    form = GestionCostumes(
        request.POST or None
    )

    if form.is_valid():

        form.save()

        return redirect('listeCostume')

    context = {
        "form": form
    }

    return render(
        request,
        'costumes/ajoutCostume.html',
        context
    )


def editCostume(request, costume_id):

    costume = Costume.objects.get(
        id=costume_id
    )

    form = GestionCostumes(
        request.POST or None,
        instance=costume
    )

    if form.is_valid():

        form.save()

        return redirect('listeCostume')

    context = {
        "form": form
    }

    return render(
        request,
        'costumes/editCostume.html',
        context
    )


def deleteCostume(request, costume_id):

    costume = Costume.objects.get(
        id=costume_id
    )

    costume.delete()

    return redirect('listeCostume')