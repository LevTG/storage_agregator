from django.contrib import admin

from .models import Company


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'city')
    fields = ['name', 'owner', 'city', 'logo', 'description', 'status']
    list_filter = ['city', 'status']
    search_fields = ['name', 'city']

    actions = ['approve_companys', 'decline_companys']

    def approve_companys(self, request, queryset):
        queryset.update(status='a')

    def decline_companys(self, request, queryset):
        queryset.update(status='d')
