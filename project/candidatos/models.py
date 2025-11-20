from django.db import models

class Candidato(models.Model):
    loja = models.CharField(max_length=100, null=True, blank=True)
    funcao = models.CharField(max_length=100,null=True, blank=True)
    nome = models.CharField(max_length=200, null=True, blank=True)
    situacao = models.CharField(max_length=50, null=True, blank=True)
    cpf = models.CharField(max_length=14, null=True, blank=True)
    email = models.EmailField(max_length=155,null=True, blank=True)
    analise = models.CharField(max_length=50, null=True, blank=True)
    certidao = models.CharField(max_length=50,null=True, blank=True)
    redacao = models.CharField(max_length=50,null=True, blank=True)
    teste_sondagem = models.CharField(max_length=255, null=True, blank=True)
    prova_matematica = models.CharField(max_length=50,null=True, blank=True)
    observacao = models.TextField(blank=True)

    def __str__(self):
        return f"{self.nome} - {self.loja}"
