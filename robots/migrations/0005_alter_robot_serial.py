# Generated by Django 3.2.16 on 2024-12-16 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('robots', '0004_alter_robot_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='robot',
            name='serial',
            field=models.CharField(default='A0001', max_length=5, verbose_name='Серийный номер'),
        ),
    ]
