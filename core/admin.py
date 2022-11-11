from django.contrib import admin
from .models import Subscribe, Involved, Statitics, Partners
# Register your models here.


class SubscribeAdmin(admin.ModelAdmin):
    list_display = ('email', 'created_at' )
    list_filter = ('email', 'created_at' )
    search_fields = ('email', 'created_at')
admin.site.register (Subscribe, SubscribeAdmin)

class InvolvedAdmin(admin.ModelAdmin):
    list_display = ('name', 'number', 'email', 'membership_type','message', 'created_at', )
    list_filter = ('name', 'created_at', 'updated_at')
    search_fields = ('name', 'created_at', 'updated_at')
admin.site.register (Involved, InvolvedAdmin)


admin.site.register (Statitics)

admin.site.register (Partners)