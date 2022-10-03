from django.contrib import admin
from django.urls import path, include

from routes.views import find_routes, home, add_route, save_route, RouteListView, RouteDetailView, RouteDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cities/', include(('cities.urls', 'cities'), namespace='cities')),
    path('trains/', include(('trains.urls', 'trains'), namespace='trains')),
    path('accounts/', include(('accounts.urls', 'accounts'), namespace='accounts')),
    path('find_routes/', find_routes, name='find_routes'),
    path('add_routes/', add_route, name='add_route'),
    path('save_routes/', save_route, name='save_route'),
    path('list/', RouteListView.as_view(), name='list'),
    path('detail/<int:pk>/', RouteDetailView.as_view(), name='detail'),
    path('delete/<int:pk>/', RouteDeleteView.as_view(), name='delete'),
    path('', home, name='home'),



]
