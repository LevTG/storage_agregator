from django.contrib import admin

from .models import Company


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'city')
    fields = ['name', 'owner', 'city']
    list_filter = ['city']
    search_fields = ['name', 'city']
