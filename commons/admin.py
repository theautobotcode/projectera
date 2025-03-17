from django.contrib import admin

from .models import Templates

@admin.register(Templates)
class ManageUserTemplates(admin.ModelAdmin):
    pass
