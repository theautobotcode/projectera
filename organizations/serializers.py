from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from organizations.models import Organization
from accounts.models import User


class OrganizationSerializer(serializers.Serializer):
    organization_name = serializers.CharField(max_length=256)
    org_slug = serializers.SlugField(max_length=256)
    address = serializers.CharField(max_length=256)
    admin_email = serializers.EmailField()

    def validate_empty_values(self, data):
        return super().validate_empty_values(data)

    def validate(self, data):
        """ 
        Check every data
        """
        if "organization_name" in data and data["organization_name"] == "":
            raise serializers.ValidationError("organization_name is required")
        if "org_slug" in data and data["org_slug"] == "":
            raise serializers.ValidationError("org_slug is required")
        if "admin_email" in data and data["admin_email"] == "":
            raise serializers.ValidationError("admin_email is required")
        obj = Organization.objects.filter(org_slug=data["org_slug"])
        if len(obj) > 0:
            raise serializers.ValidationError("org_slug must be unique")
        user = User.objects.filter(email=data["admin_email"])
        if len(user) > 0:
            raise serializers.ValidationError("user email already exists")
        return data

    def create(self, validated_data):
        org = Organization.objects.create(
            organization_name=validated_data.get("organization_name"),
            org_slug=validated_data.get("org_slug"),
            address=validated_data.get("address")

        )
        if org:
            adminuser = User(
                email=validated_data.get("admin_email")
                )
            adminuser.organization = org
            adminuser.set_password(validated_data.get("org_slug"))
            adminuser.save()
        return validated_data
