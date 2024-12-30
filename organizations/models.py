from django.db import models

class Organization(models.Model):
    orgnization_name = models.CharField(max_length=256)
    org_slug = models.SlugField(max_length=256)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        db_table="organizations"
