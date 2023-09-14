from rest_framework import serializers
from avaliacoes.models import Avaliacao
from books.api.serializer import BookSerializer

class AvaliacaoSerializer(serializers.ModelSerializer):
    # livro = BookSerializer
    
    class Meta:
        model = Avaliacao
        fields = '__all__'
