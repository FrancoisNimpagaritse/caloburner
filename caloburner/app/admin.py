from django.contrib import admin
from .models import Metric


# Configure the model for display fields
class MetricAdmin(admin.ModelAdmin):
    list_display = ('sport_day', 'distance_done')


# Register your models here.
admin.site.register(Metric)
