from django.urls import path, include
from . import views


urlpatterns = [
    path("", views.CasesView.as_view(), name='home'),
    path('detail/<int:pk>', views.HomeDetailView.as_view(), name='detail'),
]
