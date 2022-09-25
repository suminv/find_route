from django.views.generic import ListView
from routes.forms import RouteForm
from routes.models import Route


class RouteListView(ListView):
    model = Route
    template_name = 'routes/route.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        """For add context on page"""
        context = super().get_context_data(**kwargs)
        form = RouteForm()
        context['form'] = form
        return context
