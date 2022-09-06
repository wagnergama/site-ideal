from .models import Ocorrencia
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy, reverse
from .forms import OcorrenciaForms
from django.shortcuts import get_object_or_404

class OcorrenciasListView(ListView):
    template_name = 'ocorrencias_list.html'
    model = Ocorrencia
    queryset: Ocorrencia.objects.all()

class OcorrenciasCreate(CreateView):
    template_name = 'ocorrencias_create.html'
    form_class = OcorrenciaForms
    success_url = reverse_lazy('at:ocorrencia_list')
    
    def form_valid(self, form):
        return super().form_valid(form)

class OcorrenciasUpdate(UpdateView):
    template_name = 'ocorrencias_create.html'
    form_class = OcorrenciaForms
    
    def get_object(self):
        id = self.kwargs.get("id")
        return get_object_or_404(Ocorrencia, id=id)

    def form_valid(self, form):
        return super().form_valid(form)