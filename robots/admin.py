from django.contrib import admin

from robots.models import Robot


@admin.register(Robot)
class RobotAdmin(admin.ModelAdmin):
    """Модель RobotAdmin."""

    list_display = ('id', 'serial', 'model', 'version', 'created')
    search_fields = ('serial', 'model', 'version')
    list_filter = ('serial', 'model', 'version')
    list_display_links = ('id',)
