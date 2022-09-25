from django.urls import path

from routes.views import RouteListView


urlpatterns = [
    path('', RouteListView.as_view(), name='route'),
]

