from django.db import models


class Customer(models.Model):
    """Модель Customer (Покупатель)."""

    email = models.CharField(
        max_length=255,
        blank=False,
        null=False,
        verbose_name='Email')

    class Meta:
        verbose_name = 'Покупатель'
        verbose_name_plural = 'Покупатели'
        ordering = ('id',)

    def __str__(self):
        return f'Customer {self.id} with {self.email}'
