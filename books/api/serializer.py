from rest_framework import serializers
from books.models import Bosssok


class BossokSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bosssok
        fields = "__all__"
