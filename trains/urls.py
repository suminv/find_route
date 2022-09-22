from django.urls import path
from trains.views import TrainListView, TrainDetailView

urlpatterns = [
    path('', TrainListView.as_view(), name='train'),
    path('detail/<int:pk>/', TrainDetailView.as_view(), name='detail'),
    # path('update/<int:pk>/', CityUpdateView.as_view(), name='update'),
    # path('delete/<int:pk>/', CityDeleteView.as_view(), name='delete'),
    # path('add/', CityCreateView.as_view(), name='create'),
]
