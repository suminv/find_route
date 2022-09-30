from django.contrib import admin
from django.urls import path, include

from routes.views import find_routes, home, add_route

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cities/', include('cities.urls')),
    path('trains/', include(('trains.urls', 'trains'), namespace='trains')),
    path('find_routes/', find_routes, name='find_routes'),
    path('add_routes/', add_route, name='add_route'),
    path('', home, name='home'),



]
