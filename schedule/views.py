from django.contrib.auth.mixins import LoginRequiredMixin
from . import models, forms
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView


# Create your views here.
class ScheduleListView(LoginRequiredMixin ,ListView):
    model = models.Schedule
    template_name = 'schedule_list.html'
    context_object_name = 'schedules'
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        schedules = context['schedules']
        
        for schedule in schedules:
            # Get the services related to this schedule and join their names into a single string
            service_names = schedule.services.values_list('name', flat=True)
            schedule.formatted_service_names = ', '.join(service_names)
        
        return context

    def get_queryset(self):
        today = timezone.now().date()
        queryset = super().get_queryset()
        customer_name = self.request.GET.get('customer_name')
        day_schedule = self.request.GET.get('day_schedule')

        if customer_name:
            queryset = queryset.filter(customer_name__icontains=customer_name)
            return queryset
        if day_schedule:
            queryset = queryset.filter(day_schedule__icontains=day_schedule)
            return queryset
        
        return models.Schedule.objects.filter(day_schedule__date=today)


class ScheduleListCreate(LoginRequiredMixin, CreateView):
    model = models.Schedule
    template_name = 'schedule_create.html'
    form_class = forms.ScheduleForm
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    success_url = reverse_lazy('schedule_list')


class ScheduleListDetail(LoginRequiredMixin, DetailView):
    model = models.Schedule
    template_name = 'schedule_detail.html'
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Get the current schedule instance
        schedule = self.get_object()
        # Get the services related to this schedule
        service_names = schedule.services.values_list('name', flat=True)
        # Join the service names into a single string
        context['formatted_service_names'] = ', '.join(service_names)
        return context


class ScheduleListUpdate(LoginRequiredMixin, UpdateView):
    model = models.Schedule
    template_name = 'schedule_update.html'
    form_class = forms.ScheduleForm
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    success_url = reverse_lazy('schedule_list')


class ScheduleListDelete(LoginRequiredMixin, DeleteView):
    model = models.Schedule
    template_name = 'schedule_delete.html'
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    success_url = reverse_lazy('schedule_list')
