from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Resource
from .serializers import ResourceSerializer

class ResourceViewSet(viewsets.ModelViewSet):
    queryset = Resource.objects.filter(parent__isnull=True)  # Get only main menus
    serializer_class = ResourceSerializer

    @action(detail=True, methods=['get'])
    def submenus(self, request, pk=None):
        menu = self.get_object()
        submenus = menu.submenus.all()
        serializer = ResourceSerializer(submenus, many=True)
        return Response(serializer.data)
