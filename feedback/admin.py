from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from django.utils.http import urlencode

from .models import StorageFeedback, Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('email', 'text')
    fields = ['email', 'phone_number', 'text']


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
        queryset.update(status='d')
