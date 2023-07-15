from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Report(models.Model):
    employee = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='сотрудник',
        help_text='укажите сотрудника',
    )
    order = models.PositiveSmallIntegerField(
        'номер заказа покупателя',
        help_text='укажите номер заказа покупателя',
    )
    item_order = models.PositiveSmallIntegerField(
        'номер позиции в заказе покупателя',
        help_text='укажите номер позиции в заказе покупателя',
    )
    execution_time = models.PositiveSmallIntegerField(
        'время выполнения(минут)',
        help_text='укажите время выполнения в минутах',
    )
    image = models.ImageField(
        'фотография',
        upload_to='image/',
        help_text='добавьте фотографию',
    )
    report_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='время заполнения отчета',
    )

    class Meta:
        default_related_name = 'report'
        verbose_name = 'отчет'
        verbose_name_plural = 'отчеты'
