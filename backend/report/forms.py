from django import forms

from report.models import Employee, WorkReport


class DownloadReportForm(forms.ModelForm):
    class Meta:
        model = WorkReport
        employee = forms.ModelChoiceField(
            queryset=Employee.objects.all(),
            widget=forms.Select(
                attrs={
                    'cols': '100',
                    'rows': '500',
                    'class': 'form-control',
                },
            ),
        )
        fields = ('employee',)
