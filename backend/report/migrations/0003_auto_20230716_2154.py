# Generated by Django 2.2.19 on 2023-07-16 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0002_auto_20230716_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='external_id',
            field=models.PositiveIntegerField(help_text='укажите ID cотрудника в Telegram', unique=True, verbose_name='ID cотрудника в Telegram'),
        ),
    ]
