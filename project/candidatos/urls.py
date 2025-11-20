from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [

    path('', views.index, name='index'),
    path('novo/', views.novo_candidato,name='novo_candidato'),
    path('editar/<int:pk>', views.editar_candidado, name='editar_candidato'),
    path('delete/<int:id>', views.deletar_candidatos, name='deletar_candidato'),
    
]
