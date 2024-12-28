from django.contrib import admin

from orders.models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """Модель OrderAdmin."""

    list_display = ('id', 'customer', 'robot_serial')
    search_fields = ('customer', 'robot_serial')
    list_filter = ('customer', 'robot_serial')
    list_display_links = ('id',)
