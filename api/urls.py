from django.urls import path

from api.views import get_robot, get_robots_list_or_create_robot

urlpatterns = [
    path('robots/', get_robots_list_or_create_robot,
         name='robots_list_or_create_robot'),
    path('robots/<int:robot_id>/', get_robot,
         name='get_robot'),
]
