from django import forms

from report.models import Employee, Report


class DownloadReportForm(forms.ModelForm):
    class Meta:
        model = Report
        employee = forms.ModelChoiceField(
            queryset=Employee.objects.all(),
            widget=forms.Select(
                attrs={
                    'cols': '40',
                    'rows': '10',
                    'class': 'form-control',
                },
            ),
        )
        fields = ('employee',)
        # widgets = {
        #     'text': forms.Textarea(
        #         attrs={
        #             'cols': '40',
        #             'rows': '10',
        #             'class': 'form-control',
        #         },
        #     ),
        # }
