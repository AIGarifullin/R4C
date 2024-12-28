from django.db import models

from customers.models import Customer


class Order(models.Model):
    """Модель Order (Заказ)."""

    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        verbose_name='Покупатель',
        related_name='orders')
    robot_serial = models.CharField(
        max_length=5,
        blank=False,
        null=False,
        verbose_name='Серийный номер')

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ('id',)

    def __str__(self):
        return (f'Customer {self.customer} has '
                f'order {self.id} with {self.robot_serial}')
