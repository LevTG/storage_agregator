from django.contrib import admin

from .models import Storage, Manager


@admin.register(Storage)
class StorageAdmin(admin.ModelAdmin):
    list_display = ('id', 'address', 'company_owner', 'description')
    fieldsets = ((None, {'fields': ('company_owner',
                                    'address',
                                    'location',
                                    'description',
                                    'min_square',
                                    'max_square',
                                    'price',
                                    'work_hours_start',
                                    'work_hours_end',
                                    'storage_type',
                                    'warehouse_type')}),
                 ('Additions', {'fields': ('video_surveillance',
                                           'access_24h',
                                           'mobile_app',
                                           'clever_lock',
                                           'cleaning',
                                           'online_contract',
                                           'ventilation',
                                           'shipping',
                                           'wrapping',
                                           'straight_way',
                                           'any_rental_period',
                                           'inventory',
                                           'inshurance')}),
                 ('Images', {'fields': ('album',)}),
                 ('Metro', {'fields': ('metro',)}),
                 ('Status', {'fields': ('status',)}))
    list_filter = ['storage_type', 'warehouse_type', 'status']
    search_fields = ['id', 'address', 'company_owner__name', 'description']

    actions = ['approve_storages', 'decline_storages']

    def approve_storages(self, request, queryset):
        queryset.update(status='a')

    def decline_storages(self, request, queryset):
        queryset.update(status='d')

@admin.register(Manager)
class ManagerAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name')
    fieldsets = ((None, {'fields': ('first_name',
                                    'last_name',
                                    'telegram_id',
                                    'storage')}),)
