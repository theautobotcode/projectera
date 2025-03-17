from django.db import models

# Create your models here.
class Templates(models.Model):
    templatename = models.CharField(max_length=100)

    class Meta:
        db_table = "templates"
