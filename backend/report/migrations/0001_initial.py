# Generated by Django 2.2.19 on 2023-07-15 20:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveSmallIntegerField(help_text='укажите номер заказа покупателя', verbose_name='номер заказа покупателя')),
                ('item_order', models.PositiveSmallIntegerField(help_text='укажите номер позиции в заказе покупателя', verbose_name='номер позиции в заказе покупателя')),
                ('execution_time', models.PositiveSmallIntegerField(help_text='укажите время выполнения в минутах', verbose_name='время выполнения(минут)')),
                ('image', models.ImageField(help_text='добавьте фотографию', upload_to='image/', verbose_name='фотография')),
                ('report_date', models.DateTimeField(auto_now_add=True, verbose_name='время заполнения отчета')),
                ('employee', models.ForeignKey(help_text='укажите сотрудника', on_delete=django.db.models.deletion.CASCADE, related_name='report', to=settings.AUTH_USER_MODEL, verbose_name='employee')),
            ],
            options={
                'verbose_name': 'отчет',
                'verbose_name_plural': 'отчеты',
                'default_related_name': 'report',
            },
        ),
    ]
