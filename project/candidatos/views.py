from django.shortcuts import render

from candidatos.models import Candidato



def index(request):
    loja = request.GET.get('loja')
    busca = request.GET.get('busca')

    candidatos = Candidato.objects.all()

    if loja:
        candidatos = candidatos.filter(loja=loja)

    if busca:
        candidatos = candidatos.filter(nome__icontains=busca)

    lojas = Candidato.objects.values_list('loja', flat=True).distinct()

    return render(request, 'candidatos/index.html', {
        "candidatos": candidatos,
        "lojas": lojas,
    })
