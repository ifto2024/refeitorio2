from refeitorioApp.models import Aluno, Evento
from django import forms

class AlunoForms(forms.ModelForm) :
    class Meta:
        model = Aluno
        fields =['nome_aluno', 'matricula', 'foto_aluno']
        #fields = "__all__"

class EventoForms(forms.ModelForm) :
    class Meta:
        model = Evento
        fields = ['nome_evento', 'foto_evento', 'id_evento', 'id_aluno']
        #fields = "__all__"