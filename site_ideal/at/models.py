from audioop import reverse
import email
from enum import auto
from gc import get_objects
from pyexpat import model
from django.db import models
from django.urls import reverse


class CLIENTE(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=11)
    empresa = models.CharField(max_length=50)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        db_table = "tb_cliente"

class Ocorrencia (models.Model):
    problema = models.TextField(null=False, max_length=150)
    descricao = models.TextField(null=False, max_length=150)
    equipamento = models.CharField(max_length=15)
    contato = models.CharField(max_length=100)
    telefone = models.CharField(max_length=11)
    setor = models.CharField(max_length=30)
    data_abertura = models.DateTimeField(auto_now_add=True)
    ultima_atualizacao = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=11, null=False, default="Aberto") #Substituir por uma outra tabela

    def __str__(self):
        return f"{self.descricao} {self.contato} {self.celular}"

    def get_adsolute_url(self):
        return reverse("at:ocorrencias_update", kwargs={"id": self.id})

    class Meta:
        db_table = "tb_ocorrencia"