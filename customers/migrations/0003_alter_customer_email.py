# Generated by Django 3.2.16 on 2024-12-15 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0002_alter_customer_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.CharField(max_length=255, verbose_name='Email'),
        ),
    ]