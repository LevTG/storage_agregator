from django.contrib import admin

from .models import Storage


@admin.register(Storage)
class StorageAdmin(admin.ModelAdmin):
    list_display = ('id', 'address', 'owner', 'description', 'square', 'price', 'access',
                    'work_hours_start', 'work_hours_end', 'surveillance', 'climate')
    fields = ['address', 'owner', 'description', 'square', 'price', 'access',
              'work_hours_start', 'work_hours_end', 'surveillance', 'climate']
    list_filter = ['access', 'surveillance', 'climate']
    search_fields = ['address', 'owner', 'description']
