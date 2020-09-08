from django.urls import path, include
from . import views


urlpatterns = [
    path("", views.home, name='home'),
    path('detail/<int:pk>', views.HomeDetailView.as_view(), name='detail'),
]
