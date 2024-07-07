from django.contrib import admin
from .models import Technology, Project

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', )

# Register your models here.
admin.site.register(Technology)
admin.site.register(Project, ProjectAdmin)