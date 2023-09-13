from rest_framework import serializers
from books.models import Bosssok
from avaliacoes.api.serializer import AvaliacaoSerializer

class BossokSerializer(serializers.ModelSerializer):
    avalicao = AvaliacaoSerializer
    
    class Meta:
        model = Bosssok
        fields = ['autor','titulo', 'ano_lancamento', 'avaliacao']
