from django.urls import path
from trains.views import TrainListView, TrainDetailView, TrainCreateView, TrainUpdateView, TrainDeleteView

urlpatterns = [
    path('', TrainListView.as_view(), name='train'),
    path('detail/<int:pk>/', TrainDetailView.as_view(), name='detail'),
    path('update/<int:pk>/', TrainUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', TrainDeleteView.as_view(), name='delete'),
    path('add/', TrainCreateView.as_view(), name='create'),

]
