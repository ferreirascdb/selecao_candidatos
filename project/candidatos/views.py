from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from candidatos.models import Candidato
from candidatos.forms import CandidatoForm


@login_required
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
    return render(request, 'candidatos/form.html', {"form":form, "titulo": "Novo Candidato"})

def editar_candidado(request,pk):
    candidato = get_object_or_404(Candidato, pk=pk)
    if request.method == "POST":
        form = CandidatoForm(request.POST, instance=candidato)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CandidatoForm(instance=candidato)

    return render(request, 'candidatos/form.html', {"form":form, "titulo": "Editar Candidato"})

def deletar_candidatos(request, id):
    candidato = get_object_or_404(Candidato, id = id)
    if request.method == "POST":
        candidato.delete()
        return redirect('index')