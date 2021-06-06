from rest_framework.mixins import ListModelMixin
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import GenericViewSet

from books.models import Gladiator
from books.serializers import GladiatorSerializer


class GladiatorViewSet(ListModelMixin,
                       GenericViewSet):
    queryset = Gladiator.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = GladiatorSerializer

    pass
