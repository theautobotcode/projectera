from rest_framework import serializers
from .models import Resource

class ResourceSerializer(serializers.ModelSerializer):
    submenus = serializers.SerializerMethodField()

    class Meta:
        model = Resource
        fields = ["id", "name", "icon_name", "url", "submenus"]

    def get_submenus(self, obj):
        submenus = obj.submenus.all()
        return ResourceSerializer(submenus, many=True).data
