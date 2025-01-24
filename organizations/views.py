from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status

from organizations.models import Organization
from organizations.serializers import OrganizationSerializer

class CheckOrgSlug(GenericAPIView):
    '''
    Check if the organization slug exists
    '''

    def get(self, request, *args, **kwargs):
        org_slug = self.kwargs.get('slug', None)
        if org_slug:
            org = Organization.objects.filter(slug=org_slug).first()
            if org:
                return Response({'exists': True})
            return Response({'exists': False})
        else:
            return Response({"error": "Slug not provided"}, status=400)


class SetupOrganization(GenericAPIView):
    '''
    Create an organization
    '''
    serializer_class = OrganizationSerializer

    def post(self, request, *args, **kwargs):
        
        serializer = self.get_serializer(request.data)
        
        if serializer.is_valid():
            serializer.create(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        else:
            return Response(
                serializer.data,
                status=status.HTTP_400_BAD_REQUEST)
