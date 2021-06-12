from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.utils.translation import ugettext_lazy as _

from .models import Profile


@admin.register(Profile)
class ProfileAdmin(DjangoUserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'email',  'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'phone_number')}),
        (_('Permissions'), {'fields': ('is_private', 'is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
        # (_('Companies'), {'fields': ('_companies', )}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password', 'company_set'),
        }),
    )
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('username', 'email')

    def _companies(self, obj):
        return obj.company_set.all().count()
