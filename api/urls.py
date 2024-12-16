from django.urls import path

from api.views import get_robot_report, get_robots_list_or_create_robot

urlpatterns = [
    path('robots/', get_robots_list_or_create_robot,
         name='robots_list_or_create_robot'),
    path('robot-report/', get_robot_report,
         name='robot_report'),
]
