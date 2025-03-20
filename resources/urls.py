from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ResourceView,
    
)

urlpatterns = [
    path('', ResourceView.as_view()),
    

]
