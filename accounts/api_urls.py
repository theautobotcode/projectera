from django.urls import path
from .views import (
    LoginView,
    TokenRefreshView,
    TokenData

)

urlpatterns = [
    path('login', LoginView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenData.as_view(), name='token_verify'),
]