from django.contrib import messages
from django.shortcuts import render, redirect
from routes.forms import RouteForm
from routes.utils import get_routes


def home(request):
    form = RouteForm()
    return render(request, 'routes/route.html', {'form': form})


def find_routes(request):
    if request.method == 'POST':
        form = RouteForm(request.POST)
        if form.is_valid():
            try:
                context = get_routes(request, form)
            except ValueError as e:
                messages.error(request, e)
                return render(request, 'routes/route.html', {'form': form})
            return render(request, 'routes/route.html', context)
        return render(request, 'routes/route.html', {'form': form})
    else:
        form = RouteForm()
        messages.error(request, 'No data for searching')
        return render(request, 'routes/route.html', {'form': form})



def add_route(request):
    if request.method == 'POST':
        data = request.POST
        context = {}
        return render(request, 'routes/create.html', context)
    else:
        messages.error(request, "Can't save the route ...")
        return redirect('/')
