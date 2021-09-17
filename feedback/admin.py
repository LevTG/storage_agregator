from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from django.utils.http import urlencode

from .models import StorageFeedback


@admin.register(StorageFeedback)
class StorageFeedbackAdmin(admin.ModelAdmin):
    list_display = ('username', 'rating')
    list_filter = ['status', 'rating']
    fields = ['username', 'email', 'phone_number',
              'storage', 'rating', 'status', 'comments', 'created_on']

    actions = ['approve_feedbacks', 'decline_feedbacks']

    def approve_feedbacks(self, request, queryset):
        queryset.update(status='a')

    def decline_feedbacks(self, request, queryset):
        queryset.update(status='a')
