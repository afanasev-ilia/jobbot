import csv

from django.shortcuts import HttpResponse, render

from report.models import Report


def index(request):
    return render(request, 'report/index.html',)


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
