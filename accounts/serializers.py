from rest_framework import serializers
from rest_framework_simplejwt.tokens import (
    AccessToken,
    RefreshToken
)
from rest_framework.response import Response
from .models import User


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)

    def validate(self, attrs):
        return super().validate(attrs)
    

class TokenSerializers(serializers.Serializer):
    token = serializers.CharField(required=True)

    def verify(self):
        try:
            access_token = AccessToken(self.token)
            user_id = access_token['user_id']
            user = User.objects.get(id=user_id)
            return Response({'id': user.id, 'username': user.username, 'email': user.email})
        except Exception as e:
            return Response({},status=401)
        

class TokenRefreshSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    def validate(self, attrs):
        try:
            refresh = RefreshToken(attrs['refresh'])
            return {
                'access': str(refresh.access_token)
            }
        except Exception:
            raise serializers.ValidationError("Invalid refresh token")
