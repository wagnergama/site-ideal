from django.urls import path
from .views import OcorrenciasListView, OcorrenciasCreate, OcorrenciasUpdate

app_name = 'at'
urlpatterns = [
    path('', OcorrenciasListView.as_view(), name= 'ocorrencia_list'),
    path('create/', OcorrenciasCreate.as_view(), name= 'ocorrencia_create'),
    path('<int:id>/', OcorrenciasUpdate.as_view(), name= 'ocorrencia_update')
]