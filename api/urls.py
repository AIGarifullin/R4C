from django.urls import path

from api.views import (get_order, get_orders_list_or_create_order,
                       get_robot, get_robot_report,
                       get_robots_list_or_create_robot)

urlpatterns = [
    path('robots/', get_robots_list_or_create_robot,
         name='get_robots_list_or_create_robot'),
    path('robots/<int:robot_id>/', get_robot,
         name='get_robot'),
    path('robot-report/', get_robot_report,
         name='get_robot_report'),
    path('orders/', get_orders_list_or_create_order,
         name='get_orders_list_or_create_order'),
    path('orders/<int:order_id>/', get_order,
         name='get_order'),
]
