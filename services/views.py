from django.urls import reverse_lazy
from . import models, forms
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

# Create your views here.
class ServicesListView(ListView):
    model = models.Services
    template_name = 'service_list.html'
    context_object_name = 'services'
    paginate_by = 10

    def get_queryset(self):
        queryset =  super().get_queryset()
        name = self.request.GET.get('name')

        if name:
            queryset = queryset.filter(name__icontains=name)

        return queryset


class ServiceCreateView(CreateView):
    model = models.Services
    template_name = 'service_create.html'
    form_class = forms.ServiceForm
    success_url = reverse_lazy('service_list')


class ServiceUpdateView(UpdateView):
    model = models.Services
    template_name = 'service_update.html'
    form_class = forms.ServiceForm
    success_url = reverse_lazy('service_list')


class ServiceDeleteView(DeleteView):
    model = models.Services
    template_name = 'service_delete.html'
    success_url = reverse_lazy('service_list')