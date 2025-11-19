from django.shortcuts import redirect, render, get_object_or_404

from candidatos.models import Candidato
from candidatos.forms import CandidatoForm



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
def novo_candidato(request):
    if request.method == 'POST':
        form =CandidatoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        
    else:
        form = CandidatoForm()
    return render(request, 'candidatos/form.html', {"form":form})