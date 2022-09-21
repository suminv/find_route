from django.urls import path
from cities.views import CityDetailView, CityCreateView, CityUpdateView, CityDeleteView, CityListView

urlpatterns = [
    path('', CityListView.as_view(), name='cities'),
    path('detail/<int:pk>/', CityDetailView.as_view(), name='detail'),
    path('update/<int:pk>/', CityUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', CityDeleteView.as_view(), name='delete'),
    path('add/', CityCreateView.as_view(), name='create'),

]
