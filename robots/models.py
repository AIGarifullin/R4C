from django.db import models


class Robot(models.Model):
    """Модель Robot (Робот)."""

    serial = models.CharField(
        max_length=5,
        blank=False,
        null=False,
        default='R2-D2',    # model-version
        verbose_name='Серийный номер')
    model = models.CharField(
        max_length=2,
        blank=False,
        null=False,
        verbose_name='Модель')
    version = models.CharField(
        max_length=2,
        blank=False,
        null=False,
        verbose_name='Версия')
    created = models.DateTimeField(
        blank=False,
        null=False,
        verbose_name='Дата и время создания')

    class Meta:
        verbose_name = 'Робот'
        verbose_name_plural = 'Роботы'
        ordering = ('-created',)

    def __str__(self):
        return (f'Robot {self.serial}, model: {self.model} '
                f'version: {self.version}')
