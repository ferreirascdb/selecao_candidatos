from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('novo/', views.novo_candidato,name='novo_candidato'),
    path('editar/<int:pk>', views.editar_candidado, name='editar_candidato'),
]
