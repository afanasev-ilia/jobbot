import base64
from rest_framework import serializers

from report.models import Report


class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = ('employee', 'order', 'item_order', 'execution_time')
