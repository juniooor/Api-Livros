from rest_framework import viewsets
from rest_framework import permissions
from books.api.serializer import BossokSerializer
from books.models import Bosssok


class BossokViewset(viewsets.ModelViewSet):
    queryset = Bosssok.objects.all()
    serializer_class = BossokSerializer
    