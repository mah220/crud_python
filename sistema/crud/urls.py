from django.urls import path
from . import views

from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('motoristas', views.motoristas, name='motoristas'),
    path('veiculos', views.veiculos, name='veiculos'),
    path('controle', views.controles, name='controle'),

    ###############
    # VEICULOS
    ###############

    path('veiculos/cadastro', views.cadastro, name='cadastro'),
    path('veiculos/visualizar/<int:id>', views.visualizar, name='visualizar'),
    path('veiculos/editar', views.editar, name='editar'),
    path('veiculos/editar/<int:id>', views.editar, name='editar'),

    ###############
    # EXCLUIR 
    ###############

    path('excluir_controle/<int:id>', views.excluir_controle, name='excluir_controle'),
    path('excluir_motorista/<int:id>', views.excluir_motorista, name='excluir_motorista'),
    path('excluir/<int:id>', views.excluir, name='excluir'),

    ###############
    # MOTORISTAS
    ###############
    
    path('motoristas/cadastro', views.cadastro_motorista, name='cadastro_motoristas'),
    path('motoristas/editar/<int:id>', views.editar_motorista, name='editar_motoristas'),
    path('motoristas/visualizar/<int:id>', views.visualizar_motorista, name='visualizar_motoristas'),

    ###############
    # CONTROLE
    ###############

    path('controle/cadastro', views.cadastro_controle, name='cadastro_controle'),
    path('controle/editar/<int:id>', views.editar_controle, name='editar_controle'),
    path('controle/visualizar/<int:id>', views.visualizar_controle, name='visualizar_controle'),

    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

 