# Generated by Django 4.2.3 on 2023-08-01 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0005_alter_report_employee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='image',
            field=models.FilePathField(path='/media/image'),
        ),
    ]
