from django.urls import path

from . import views


urlpatterns = [
    path("", views.GiftsView.as_view()),
    # path("<slug:slug>/", views.GiftDetailView.as_view(), name='gift_detail'),
    path("comment/<int:pk>/", views.AddComment.as_view(), name='add_comment'),
    path("map/", views.index, name='index'),
]
