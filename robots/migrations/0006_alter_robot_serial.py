# Generated by Django 3.2.16 on 2024-12-17 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('robots', '0005_alter_robot_serial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='robot',
            name='serial',
            field=models.CharField(default='R2_D2', max_length=5, verbose_name='Серийный номер'),
        ),
    ]