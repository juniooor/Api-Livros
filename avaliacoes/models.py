from django.db import models
from django.contrib.auth.models import User
from books.models import Bosssok
# Create your models here.

class Avaliacao(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    comentario = models.TextField(max_length=490)
    data = models.DateField(auto_now_add=True)
    stars = models.DecimalField(max_digits=10, decimal_places=3 )
    models.ForeignKey(Bosssok, on_delete=models.CASCADE, related_name = "livros")
    def __str__(self):
        return self.usuario.username 