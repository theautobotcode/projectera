from django.contrib import admin

# Register your models here.
from .models import Resource

@admin.register(Resource)
class ManageResource(admin.ModelAdmin):
    pass