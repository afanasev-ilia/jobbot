import csv

from datetime import datetime
from datetime import timedelta
from openpyxl import Workbook

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
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
    )
    response['Content-Disposition'] = 'attachment; filename={date}-movies.xlsx'.format(
        date=datetime.now().strftime('%Y-%m-%d'),
    )
    workbook = Workbook()

    # Get active worksheet/tab
    worksheet = workbook.active
    worksheet.title = 'reports'

    # Define the titles for columns
    columns = [
        'order',
        'item_order',
        'execution_time',
        'report_date',
    ]
    row_num = 1

    # Assign the titles for each cell of the header
    for col_num, column_title in enumerate(columns, 1):
        cell = worksheet.cell(row=row_num, column=col_num)
        cell.value = column_title

    # Iterate through all movies
    for report in reports:
        row_num += 1
        
        # Define the data for each cell in the row 
        row = [
            report.order,
            report.item_order,
            report.execution_time,
            report.report_date,
        ]
        
        # Assign the data for each cell of the row 
        for col_num, cell_value in enumerate(row, 1):
            cell = worksheet.cell(row=row_num, column=col_num)
            cell.value = cell_value

    workbook.save(response)




    # response = HttpResponse(
    #     reports,
    #     content_type='application/vnd.ms-excel;charset=utf-8',
    # )
    # response['Content-Disposition'] = 'attachment; filename="reports.xls"'

    # writer = csv.writer(response)
    # writer.writerow(['employee', 'order'])
    # for report in reports:
    #     writer.writerow([report.employee, report.order])

    return response
