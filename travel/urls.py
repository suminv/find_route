from django.contrib import admin
from django.urls import path, include

from cities.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('cities/', include('cities.urls')),
    path('trains/', include(('trains.urls', 'trains'), namespace='trains')),

]
