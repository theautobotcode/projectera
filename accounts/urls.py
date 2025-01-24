from django.urls import path
from .views import loginpage
urlpatterns =[
    path('login',loginpage, name="loginpage"),
]