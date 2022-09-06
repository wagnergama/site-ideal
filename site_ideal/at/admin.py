from django.contrib import admin
from .models import CLIENTE, Ocorrencia

# Register your models here.

@admin.register(CLIENTE)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ["id", "first_name", "last_name", "email"]

@admin.register(Ocorrencia)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ["problema", "descricao", "data_abertura", "ultima_atualizacao", "status"]