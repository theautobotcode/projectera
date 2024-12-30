from django.db import models

class Organization(models.Model):
    orgnization_name=models.CharField(max_length=256)
    org_slug=models.SlugField(max_length=256)
    address=models.TextField()


    class Meta:
        db_table="organizations"
