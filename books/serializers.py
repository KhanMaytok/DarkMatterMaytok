from rest_framework import serializers

from books.models import Gladiator


class GladiatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gladiator
        fields = '__all__'
