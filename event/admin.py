from django.contrib import admin
from .models import Event, EventCreator, EventAttendence


# Register your models here.
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'teacher', 'date_of_start', 'date_of_end','about')

admin.site.register(EventCreator)
admin.site.register(EventAttendence)
