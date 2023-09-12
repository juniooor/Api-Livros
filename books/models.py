from django.db import models
from avaliacoes.models import Avaliacao

# Create your models here.
class Bosssok(models.Model):
    autor = models.CharField(max_length=50)
    titulo = models.CharField(max_length=90)
    ano_lancamento = models.IntegerField()
    avalicao = models.ManyToManyField(Avaliacao, )
    
    
    def __str__(self):
        return self.titulo
     