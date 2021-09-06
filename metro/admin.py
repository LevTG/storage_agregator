from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from django.utils.http import urlencode

from .models import Station, Line


@admin.register(Station)
class StationAdmin(admin.ModelAdmin):
    list_display = ('name', 'line')
    list_filter = ['line']
    search_fields = ['name', 'line']
    fields = ['name', 'line', 'code_name'] # 'line__color']



@admin.register(Line)
class LineAdmin(admin.ModelAdmin):
    list_display = ('name', 'view_stations_link')

    search_fields = ['name']

    fieldsets = (
        (None, {'fields': ('name', 'color', )}),
    )

    def view_stations_link(self, obj):
        count = obj.station_set.count()
        url = (
                reverse("admin:metro_line_changelist")
                + "?"
                + urlencode({"station__id": f"{obj.id}"})
        )
        return format_html('<a href="{}">{} Stations</a>', url, count)

    view_stations_link.short_description = "Stations"
