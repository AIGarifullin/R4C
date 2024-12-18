import json

import pytest
from django.test import Client

from customers.models import Customer
from orders.models import Order
from robots.models import Robot


MODEL = 'R2'
VERSION = 'D2'
CREATED = '2022-06-06T12:05:10Z'
robot_data = dict(
    model=MODEL,
    version=VERSION,
    created=CREATED
)
json_robot_data = json.dumps(robot_data)

CUSTOMER = 1
ROBOT_SERIAL = 'R2-D2'
order_data = dict(
    customer=CUSTOMER,
    robot_serial=ROBOT_SERIAL
)
json_order_data = json.dumps(order_data)


@pytest.fixture
def client():
    """Создать модель пользователя Клиент."""
    return Client(username='Клиент')


@pytest.fixture
def robot():
    """Создать объект robot класса Robot."""
    return Robot.objects.create(
        serial='R2-D2',
        model='R2',
        version='D2',
        created='2022-06-06T12:05:10Z'
    )


@pytest.fixture
def customer():
    """Создать объект customer класса Customer."""
    return Customer.objects.create(
        email='customer@mail.ru'
    )


@pytest.fixture
def order(customer):
    """Создать объект order класса Order."""
    return Order.objects.create(
        customer=customer,
        robot_serial='R2-D2'
    )
