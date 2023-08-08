import csv

from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from report.serializers import ReportSerializer
from report.models import Report


@api_view(['POST'])
def report_list(request):
    if request.method == 'POST':
        serializer = ReportSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def export_excel(request):
    reports = Report.objects.all()
    response = HttpResponse(
        reports,
        content_type='application/vnd.ms-excel;charset=utf-8',
    )
    response['Content-Disposition'] = 'attachment; filename="reports.xls"'

    writer = csv.writer(response)
    writer.writerow(['employee', 'order'])
    for report in reports:
        writer.writerow([report.employee, report.order])

    return response
