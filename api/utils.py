from django.utils import timezone

models_list = ['R2', '11', '12', '13', 'X5']


def validate_robot_data(data):
    """Валидация данных о роботе."""
    required_fields = ['model', 'version', 'created']
    for field in required_fields:
        if field not in data:
            return False, f'Missing field {field}'
    if data['model'] not in models_list:
        return False, f'Not existing model {data["model"]}'
    return True, None


end_date = timezone.now()
start_date = end_date - timezone.timedelta(days=7)
