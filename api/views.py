import http
import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from api.utils import validate_robot_data
from robots.models import Robot


@csrf_exempt   # Отключили механизм защиты от межсайтовой подделки запросов
def get_robots_list_or_create_robot(request):
    """Получение списка роботов и их создание."""
    if request.method == 'GET':
        robots = Robot.objects.all().values('id', 'serial', 'model',
                                            'version', 'created')
        robots_list = list(robots)
        return JsonResponse(
            robots_list, safe=False, status=http.HTTPStatus.OK
            )
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            is_valid, error_message = validate_robot_data(data)
            
            if not is_valid:
                return JsonResponse(
                    {'error': error_message},
                    status=http.HTTPStatus.BAD_REQUEST
                    )
            robot = Robot(
                model=data['model'],
                version=data['version'],
                created=data['created'],
            )
            robot.save()
            return JsonResponse(
                {'message': 'Robot created', 'robot_id': robot.id},
                status=http.HTTPStatus.CREATED
                )
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'},
                                status=http.HTTPStatus.BAD_REQUEST
            )
    return JsonResponse(
        {'error': 'Only GET and POST requests are allowed.'},
        status=http.HTTPStatus.METHOD_NOT_ALLOWED
        )