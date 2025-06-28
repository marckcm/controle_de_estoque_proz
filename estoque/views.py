from django.shortcuts import render, get_object_or_404
from .models import Material, Movimentacao

def home(request):
    return render(request, 'estoque/home.html')

def lista_materiais(request):
    materiais = Material.objects.all()
    return render(request, 'estoque/lista_materiais.html', {'materiais': materiais})

def detalhe_material(request, pk):
    material = get_object_or_404(Material, pk=pk)
    movimentacoes = Movimentacao.objects.filter(material=material)
    return render(request, 'estoque/detalhe_material.html', {'material': material, 'movimentacoes': movimentacoes})

def lista_movimentacoes(request):
    movimentacoes = Movimentacao.objects.all()
    return render(request, 'estoque/movimentacoes.html', {'movimentacoes': movimentacoes})
