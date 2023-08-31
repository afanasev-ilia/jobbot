import csv

from django.shortcuts import HttpResponse, render, get_object_or_404
from django.http import HttpRequest

from report.forms import DownloadReportForm
from report.models import Employee


def index(request):
    form = DownloadReportForm()
    return render(request, 'report/index.html', {'form': form})


def download_report(request: HttpRequest) -> HttpResponse:
    employee = get_object_or_404(Employee, id=request.POST.get('employee'))
    reports = employee.work_report.select_related('employee')
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
