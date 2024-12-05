from django.shortcuts import render, get_object_or_404, redirect
from django.shortcuts import render 
from refeitorioApp.forms import AlunoForms
from refeitorioApp.models import Aluno
from refeitorioApp.forms import Evento
from refeitorioApp.forms import EventoForms


def opcoes_views(request):
    return render(request, 'refeitorio/opcoes_views.html')


def home (request):
    form = AlunoForms
    context = {'form':form}
    return render(request, 'refeitorio/new_aluno.html', context)


def new_aluno(request):
    alunos = Aluno.objects.all()
    form = AlunoForms(request.POST, request.FILES)
    if request.method == "POST":

          if form.is_valid():
             aluno = form.save()
             aluno.save()
             form = AlunoForms()
    context={'form': form, 'alunos':alunos}
    return render(request, 'refeitorio/new_aluno.html', context)


def editar_aluno(request, id, form=None):
    alunos = Aluno.objects.all()
    aluno = get_object_or_404(Aluno, pk=id)
    form = AlunoForms(instance=aluno)
    if (request.method=='POST'):
        form = AlunoForms(request.POST, request.FILES, instance=aluno)
        if form.is_valid():
            form.save()
            return redirect('new_aluno')
        else:
            return render(request,'refeitorio/editar_aluno.html',{'form':form, 'alunos':alunos})
    else:
        return render(request, 'refeitorio/editar_aluno.html',{'form':form, 'alunos':alunos})
    
    
def excluir_aluno(request, id):
    aluno = get_object_or_404(Aluno, pk=id)
    form = AlunoForms(instance=aluno)
    alunos = Aluno.objects.all()
    if (request.method=='POST'):
        aluno.delete()
        return redirect('new_aluno')
    else:
        return render(request, 'refeitorio/excluir_aluno.html',{'aluno':aluno, 'alunos':alunos, 'form':form})
    
    
#Eventos

def cadastrar_evento(request):
    form = EventoForms(request.POST, request.FILES)
    eventos = Evento.objects.all()
    if request.method == "POST":

          if form.is_valid():
             evento = form.save()
             evento.save()
             form = EventoForms()
    context={'form': form, 'eventos':eventos}
    return render(request, 'refeitorio/cadastrar_evento.html', context)

def editar_evento(request, id, form=None):
    eventos = Evento.objects.all()
    evento = get_object_or_404(Evento, pk=id)
    form = EventoForms(instance=evento)
    if (request.method=='POST'):
        form = EventoForms(request.POST, request.FILES, instance=evento)
        if form.is_valid():
            form.save()
            return redirect('cadastrar_evento')
        else:
            return render(request,'refeitorio/editar_evento.html',{'form':form, 'eventos':eventos})
    else:
        return render(request, 'refeitorio/editar_evento.html',{'form':form, 'eventos':eventos})
    
def excluir_evento(request, id):
    evento = get_object_or_404(Evento, pk=id)
    form = EventoForms(instance=evento)
    eventos = Evento.objects.all()
    if (request.method=='POST'):
        evento.delete()
        return redirect('cadastrar_evento')
    else:
        return render(request, 'refeitorio/excluir_evento.html',{'evento':evento, 'eventos':eventos, 'form':form})