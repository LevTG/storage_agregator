from django.contrib import admin

from .models import Application


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number', 'text', 'status', 'storage')
    fields = ['name', 'email', 'phone_number', 'text', 'status', 'storage', 'recipient']
    list_filter = [('status')]
    search_fields = ['text', 'storage']

    actions = ['approve_applications', 'decline_applications']

    def approve_applications(self, request, queryset):
        queryset.update(status='a')

    def decline_applications(self, request, queryset):
        queryset.update(status='d')
