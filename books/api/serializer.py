from rest_framework import serializers
from books.models import Book
from avaliacoes.models import Avaliacao
class BookSerializer(serializers.ModelSerializer):
    avaliacao = Avaliacao
    class Meta:
        model = Book
        fields = ['id','autor','titulo', 'ano_lancamento','avaliacao' ]
