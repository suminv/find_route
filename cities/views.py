from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView
from django.contrib.messages.views import SuccessMessageMixin
from cities.forms import CityForm
from cities.models import City


class CityCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = City
    form_class = CityForm
    template_name = 'cities/create.html'
    success_url = reverse_lazy('cities:cities')
    success_message = "%(name)s was created successfully!"


class CityUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = City
    form_class = CityForm
    template_name = 'cities/update.html'
    success_url = reverse_lazy('cities:cities')
    success_message = "%(name)s was updated successfully!"


class CityDetailView(DetailView):
    queryset = City.objects.all()
    template_name = 'cities/detail.html'
    success_url = reverse_lazy('cities:cities')



class CityDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = City
    template_name = 'cities/delete.html'
    success_url = reverse_lazy('cities:cities')
    success_message = 'City was deleted successfully!'

    def get_success_message(self, cleaned_data):
        """Alert message for delete city."""
        return self.success_message


class CityListView(ListView):
    paginate_by = 2
    model = City
    template_name = 'cities/city.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        """For add context on page"""
        context = super().get_context_data(**kwargs)
        form = CityForm()
        context['form'] = form
        return context

