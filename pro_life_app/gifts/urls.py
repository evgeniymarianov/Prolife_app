from django.urls import path, include

from . import views


urlpatterns = [
    path("", views.GiftsView.as_view()),
    path('api-all/', views.gift_list),
    path('api-detail/<int:pk>/', views.gift_detail),
    # path("<slug:slug>/", views.GiftDetailView.as_view(), name='gift_detail'),
    path("comment/<int:pk>/", views.AddComment.as_view(), name='add_comment'),
    path("map/", views.index, name='index'),
]
