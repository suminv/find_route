from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView

from cities.forms import HtmlForm, CityForm
from cities.models import City


def index(request):
    return render(request, 'cities/index.html')


def cities(request, pk=None):
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            form.save()

    form = CityForm()
    city = City.objects.all()
    context = {'cities': city, 'form': form}
    return render(request, 'cities/city.html', context)


class CityCreateView(CreateView):
    model = City
    form_class = CityForm
    template_name = 'cities/create.html'


class CityUpdateView(UpdateView):
    model = City
    form_class = CityForm
    template_name = 'cities/update.html'



class CityDetailView(DetailView):
    queryset = City.objects.all()
    template_name = 'cities/detail.html'
    success_url = reverse_lazy('cities')


class CityDeleteView(DeleteView):
    model = City
    template_name = 'cities/delete.html'
    success_url = reverse_lazy('cities')

