from django.db import models


class Employee(models.Model):
    external_id = models.PositiveIntegerField(
        'ID cотрудника в Telegram',
        unique=True,
        help_text='укажите ID cотрудника в Telegram',
    )
    full_name = models.CharField(
        'ФИО сотрудника',
        max_length=150,
        help_text='укажите ФИО cотрудника',
    )
    name = models.CharField(
        'ФИО сотрудника латиницей',
        max_length=150,
        help_text='укажите имя cотрудника латиницей',
    )

    class Meta:
        default_related_name = 'employee'
        verbose_name = 'сотрудник'
        verbose_name_plural = 'сотрудники'

    def __str__(self) -> str:
        return self.name


class WorkReport(models.Model):
    employee = models.ForeignKey(
        Employee,
        on_delete=models.PROTECT,
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
        blank=True,
        upload_to='image/',
        help_text='добавьте фотографию',
    )
    report_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='время заполнения отчета',
    )

    class Meta:
        default_related_name = 'work_report'
        verbose_name = 'отчет о работе'
        verbose_name_plural = 'отчеты о работе'


class CleanReport(models.Model):
    employee = models.ForeignKey(
        Employee,
        on_delete=models.PROTECT,
        verbose_name='сотрудник',
        help_text='укажите сотрудника',
    )
    image = models.ImageField(
        'фотография',
        blank=True,
        upload_to='image/',
        help_text='добавьте фотографию',
    )
    report_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='время заполнения отчета',
    )

    class Meta:
        default_related_name = 'clean_report'
        verbose_name = 'отчет об уборке'
        verbose_name_plural = 'отчеты об уборке'
