from django.urls import path

from .views import (
    CheckOrgSlug,
)

urlpatterns = [
    path('check-slug/<slug:slug>/', CheckOrgSlug.as_view(), name='check-slug'),
]