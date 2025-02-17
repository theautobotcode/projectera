from django.db import models
from organizations.models import Organization


class OrgModelMixins(models.Model):
    organization_id = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE)
    
    class Meta:
        abstract = True

    @classmethod
    def get_by_org(cls, org):
        if isinstance(org, Organization):
            obj = cls.objects.filter(organization_id=org)
            if len(obj) != 0:
                return obj.first()
        elif isinstance(org, int):
            org = Organization.objects.filter(pk=org)
            if len(org) != 0:
                obj = cls.objects.filter(organization_id=org.first())
                if len(obj) != 0:
                    return obj.first()
        return
    
    @classmethod
    def filter_by_org(cls, org):
        if isinstance(org, Organization):
            obj = cls.objects.filter(organization_id=org)
            if len(obj) != 0:
                return obj.all()
        elif isinstance(org, int):
            org = Organization.objects.filter(pk=org)
            if len(org) != 0:
                obj = cls.objects.filter(organization_id=org.first())
                if len(obj) != 0:
                    return obj.all()
        return


class TimeStampMixins(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        abstract = True
