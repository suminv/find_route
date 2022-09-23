from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, DetailView, CreateView

from trains.forms import TrainForm
from trains.models import Train


class TrainListView(ListView):
    paginate_by = 3
    model = Train
    template_name = 'trains/train.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        """For add context on page"""
        context = super().get_context_data(**kwargs)
        return context


class TrainDetailView(DetailView):
    queryset = Train.objects.all()
    template_name = 'trains/detail.html'
    success_url = reverse_lazy('trains:detail')


class TrainCreateView(SuccessMessageMixin, CreateView):
    model = Train
    form_class = TrainForm
    template_name = 'trains/create.html'
    success_message = "%(name)s was created successfully!"
