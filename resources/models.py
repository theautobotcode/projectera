from django.db import models

class Resource(models.Model):
    name = models.CharField(max_length=255)
    icon_name = models.CharField(max_length=100, blank=True, null=True)  # Icon class name
    url = models.CharField(max_length=255, blank=True, null=True)  # Navigation URL
    parent = models.ForeignKey(
        'self', on_delete=models.CASCADE, null=True, blank=True, related_name='submenus'
    )

    class Meta:
        db_table = "resource"  # Set table name

    def __str__(self):
        return self.name
