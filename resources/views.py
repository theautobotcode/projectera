from rest_framework.generics import ListAPIView
from rest_framework.mixins import ListModelMixin
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from .models import Resource
from .serializers import ResourceSerializer

class ResourceView(ListAPIView):
    queryset = Resource.objects.filter(parent__isnull=True)  # Get only main menus
    serializer_class = ResourceSerializer
    permission_classes = [ IsAuthenticatedOrReadOnly ]

