from django.contrib import admin
from .models import Projects
# Register your models here.

class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'created_at' )
    list_filter = ('title', 'description', 'created_at' )
    search_fields = ('title', 'description', 'created_at')
admin.site.register (Projects, ProjectsAdmin)