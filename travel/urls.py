from django.contrib import admin
from django.urls import path, include

from routes.views import find_routes, home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cities/', include('cities.urls')),
    path('trains/', include(('trains.urls', 'trains'), namespace='trains')),
    path('find_routes/', find_routes, name='find_routes'),
    path('', home, name='home'),


]
