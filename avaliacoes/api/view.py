from rest_framework import viewsets
from rest_framework import permissions
from avaliacoes.api.serializer import AvaliacaoSerializer
from avaliacoes.models import Avaliacao


class AvaliacaoViewset(viewsets.ModelViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer
    