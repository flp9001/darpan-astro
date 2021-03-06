from django.contrib import admin

# Register your models here.
from .models import Chart


class ChartAdmin(admin.ModelAdmin):
    list_display = ('name', 'datetime_utc', 'owner', 'country', 'city', 'slug')
    readonly_fields = ('datetime_utc', 'slug')

    autocomplete_fields = ['country', 'city',]

admin.site.register(Chart, ChartAdmin)
