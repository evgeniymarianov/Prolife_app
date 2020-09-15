from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
    path("", views.GiftsView.as_view()),
    path('api-all/', views.GiftList.as_view()),
    path('api-detail/<int:pk>/', views.GiftDetail.as_view()),
    path('comment/', views.CommentCreateView.as_view()),
    # path("<slug:slug>/", views.GiftDetailView.as_view(), name='gift_detail'),
    path("comment/<int:pk>/", views.AddComment.as_view(), name='add_comment'),
    path("map/", views.index, name='index'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
