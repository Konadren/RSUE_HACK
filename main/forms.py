from django.forms import ModelForm, DateInput
from .models import Date


class DateForm(ModelForm):
    class Meta:
        model = Date
        fields = ['start_date', 'end_date']

        widgets = {
            "start_date" : DateInput,
            "end_date" : DateInput
        }