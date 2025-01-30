from django.urls import path

from .views import (
    CheckOrgSlug,
    SetupOrganization
)

urlpatterns = [
    path('check-slug/<slug:slug>/', CheckOrgSlug.as_view(), name='check-slug'),
    path('setup-org/', SetupOrganization.as_view(), name='org-setup'),
]