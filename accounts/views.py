from django.shortcuts import render
from django.contrib.auth import login,logout,authenticate
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny

from accounts.serializers import LoginSerializer


class LoginView(GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]
    
    def post(self,request):
        print("==================")
        print(request.data)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.data
        user = authenticate(request,username=data['email'],password=data['password'])
        if user:
            login(request,user)
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'org_slug':user.organization.org_slug if user.organization else None 
            })
        else:
            return Response({"msg":"Invalid Credentials"}, status=400)


def loginpage(r):
    return render(r, "login.html")