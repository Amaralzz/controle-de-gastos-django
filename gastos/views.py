from django.shortcuts import render, redirect
from .models import Gasto
from .forms import GastoForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

@login_required
def listar_gastos(request):
    gastos = Gasto.objects.filter(usuario = request.user)
    return render(request, 'gastos/lista.html', {'gastos': gastos})

@login_required
def criar_gastos(request):
    if request.method == 'POST':
        form = GastoForm(request.POST)
        if form.is_valid():
            novo_gasto = form.save(commit=False)
            novo_gasto.usuario = request.user
            novo_gasto.save()
            return redirect('listar_gastos')
    else:
        form = GastoForm()
    return render(request, 'gastos/criar.html', {'form':form})

@login_required
def editar_gasto(request, gasto_id):
    gasto = get_object_or_404(Gasto, id = gasto_id, usuario =  request.user)
    if request.method == 'POST':
        form = GastoForm(request.POST, instance= gasto)
        if form.is_valid():
            form.save()
            return redirect('listar_gastos')
    else:
        form = GastoForm(instance=gasto)
    return render(request, 'gastos/editar.html', {'form':form})

@login_required
def excluir_gasto(request, gasto_id):
    gasto = get_object_or_404(Gasto, id = gasto_id, usuario = request.user)
    if request.method == 'POST':
        gasto.delete()
        return redirect('listar_gastos')
    else: 
        return redirect('listar_gastos')
