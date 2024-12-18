from http import HTTPStatus

import pytest
from django.urls import reverse

from orders.models import Order
from robots.models import Robot

from .conftest import (CREATED, MODEL, ROBOT_SERIAL,
                       VERSION, json_order_data,
                       json_robot_data)


@pytest.mark.django_db
def test_get_robots_list(client):
    """Проверить получение списка роботов."""
    url = reverse('get_robots_list_or_create_robot')
    response = client.get(url)
    assert response.status_code == HTTPStatus.OK


@pytest.mark.django_db
def test_get_robot(client, robot):
    """Проверить получение робота по ID."""
    url = reverse('get_robot', args=[robot.id])
    response = client.get(url)
    assert response.status_code == HTTPStatus.OK
    assert response.json()['id'] == robot.id


@pytest.mark.django_db
def test_create_robot(client, robot):
    """Проверить возможность создания робота."""
    robot.delete()
    init_robots_count = Robot.objects.count()
    url = reverse('get_robots_list_or_create_robot')
    response = client.post(url, data=json_robot_data,
                           content_type='application/json')
    assert response.status_code == HTTPStatus.CREATED
    assert Robot.objects.count() == init_robots_count + 1
    assert robot.model == MODEL
    assert robot.version == VERSION
    assert robot.created == CREATED


@pytest.mark.django_db
def test_get_orders_list(client):
    """Проверить получение списка заказов."""
    url = reverse('get_orders_list_or_create_order')
    response = client.get(url)
    assert response.status_code == HTTPStatus.OK


@pytest.mark.django_db
def test_get_order(client, order):
    """Проверить получение заказа по ID."""
    url = reverse('get_order', args=[order.id])
    response = client.get(url)
    assert response.status_code == HTTPStatus.OK
    assert response.json()['id'] == order.id


@pytest.mark.django_db
def test_create_order(client, order, customer):
    """Проверить возможность создания клиентом заказа."""
    # order.delete()
    init_orders_count = Order.objects.count()
    print(init_orders_count)
    url = reverse('get_orders_list_or_create_order')
    response = client.post(url, data=json_order_data,
                           content_type='application/json')
    assert response.status_code == HTTPStatus.CREATED
    assert Order.objects.count() == init_orders_count + 1
    assert order.customer_id == customer.id
    assert order.robot_serial == ROBOT_SERIAL
