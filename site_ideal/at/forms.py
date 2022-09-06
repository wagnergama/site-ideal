from socket import fromshare
from django import forms
from .models import Ocorrencia

class OcorrenciaForms(forms.ModelForm):
    problema = forms.CharField()
    descricao = forms.CharField()
    equipamento = forms.CharField()
    contato = forms.CharField()
    telefone = forms.CharField()
    setor = forms.CharField()

    class Meta:
        model = Ocorrencia
        fields = (
            "problema",
            "descricao",
            "equipamento",
            "contato",
            "telefone",
            "setor",
        )
