from django.contrib import admin
from .models import Subscribe
# Register your models here.


class SubscribeAdmin(admin.ModelAdmin):
    list_display = ('email', 'created_at' )
    list_filter = ('email', 'created_at' )
    search_fields = ('email', 'created_at')
admin.site.register (Subscribe, SubscribeAdmin)