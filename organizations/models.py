from django.db import models
from django.dispatch import receiver
# from utils.mongoclient import MongoDBClient

class Organization(models.Model):
    organization_name = models.CharField(max_length=256)
    org_slug = models.SlugField(max_length=256, unique=True)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    
    class Meta:
        db_table="organizations"

    def __str__(self):
        return self.organization_name

# @receiver(models.signals.post_save, sender=Organization)
# def manage_organization(sender, instance, created, **kwargs):
#     client= MongoDBClient()
#     if created:
#         client.insert("organizations", instance.__dict__)
        
#     else:
#         query = {"id": instance.pk}  # Use `id` (or `_id` if using MongoDB's ObjectId)
#         client.update("organizations", query, {"$set": instance.__dict__})
