import base64
from django.core.files.base import ContentFile
from rest_framework import serializers

from report.models import CleanReport, WorkReport


class Base64ImageField(serializers.ImageField):
    def to_internal_value(self, data):
        if isinstance(data, str) and data.startswith('data:image'):
            format, imgstr = data.split(';base64,')
            ext = format.split('/')[-1]
            data = ContentFile(base64.b64decode(imgstr), name='temp.' + ext)

        return super().to_internal_value(data)


class WorkReportSerializer(serializers.ModelSerializer):
    image = Base64ImageField(required=False, allow_null=True)

    class Meta:
        model = WorkReport
        fields = ('employee', 'order', 'item_order', 'execution_time', 'image')


class CleanReportSerializer(serializers.ModelSerializer):
    image = Base64ImageField(required=False, allow_null=True)

    class Meta:
        model = CleanReport
        fields = ('employee', 'image')
