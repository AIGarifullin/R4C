from datetime import timedelta
from django.utils import timezone


models_list = ['R2', '11', '12', '13', 'X5']

end_date = timezone.now()
start_date = end_date - timedelta(days=7)

Email_subject = 'Information about the sale of the robot'
Email_text = """Добрый день!
Недавно вы интересовались нашим роботом модели {}, версии {}.
Этот робот теперь в наличии. Если вам подходит этот вариант - пожалуйста,
свяжитесь с нами"""


def validate_robot_data(data):
    """Валидация данных о роботе."""
    required_fields = ['model', 'version', 'created']
    for field in required_fields:
        if field not in data:
            return False, f'Missing field {field}'
    if data['model'] not in models_list:
        return False, f'Not existing model {data["model"]}'
    return True, None


def validate_order_data(data):
    """Валидация данных о заказе."""
    required_fields = ['customer', 'robot_serial']
    for field in required_fields:
        if field not in data:
            return False, f'Missing field {field}'
    return True, None
