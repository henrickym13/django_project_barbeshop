from django import forms
from .models import Schedule


class ScheduleForm(forms.ModelForm):

    class Meta:
        model = Schedule
        fields = ['customer_name', 'services', 'day_schedule', 'time_schedule']
        widgets = {
            'services': forms.CheckboxSelectMultiple(),
            'day_schedule': forms.DateTimeInput(attrs={'type': 'date'}),
        }
        labels = {
            'customer_name': 'Nome',
            'services': 'Serviços',
            'day_schedule': 'Dia',
            'time_schedule': 'Horário',
        }