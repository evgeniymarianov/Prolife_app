from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.base import View
from django.http import HttpResponse, JsonResponse, Http404
from rest_framework.parsers import JSONParser
from gifts.serializers import (
    AddressListSerializer,
    GiftListSerializer,
    CommentCreateSerializer,
)
from rest_framework import mixins, generics, permissions, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import Gift, Category, GiftAddress
from .forms import CommentForm
from .service import GiftFilter


class GiftViewSet(viewsets.ReadOnlyModelViewSet):
    """Вывод списка фильмов"""
    filter_backends = (DjangoFilterBackend,)
    filterset_class = GiftFilter
    queryset = Gift.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return GiftListSerializer
        elif self.action == "retrieve":
            return GiftDetailSerializer

# class AddressListView(generics.ListAPIView):
#     """Вывод списка адресов даров"""
#     queryset = GiftAddress.objects.all()
#     serializer_class = AddressListSerializer
#
#
# class GiftList(generics.ListCreateAPIView):
#     """
#     List all code gifts, or create a new gift.
#     """
#     queryset = Gift.objects.all()
#     serializer_class = GiftListSerializer
#     filter_backends = (DjangoFilterBackend,)
#     filterset_class = GiftFilter
#     permission_classes = [permissions.IsAuthenticated]
#
#
# class GiftDetail(generics.RetrieveAPIView):
#     """
#     Retrieve, update or delete a code gift.
#     """
#     queryset = Gift.objects.all()
#     serializer_class = GiftListSerializer
#     permission_classes = [permissions.IsAuthenticated]
#
# class CommentCreateView(generics.CreateAPIView):
#     """Добавление отзыва"""
#     serializer_class = CommentCreateSerializer
#
# class GiftsView(ListView):
#     """Список Даров"""
#     model = Gift
#     queryset = Gift.objects.all()
#

#class GiftDetailView(DetailView):
#    """Полное описание Дара"""
#    model = Gift
#    slug_field = "url"


# class AddComment(View):
#     """Отзыв"""
#     def post(self, request, pk):
#         form = CommentForm(request.POST)
#         gift = Gift.objects.get(id=pk)
#         if form.is_valid():
#             form = form.save(commit=False)
#             if request.POST.get("parent", None):
#                 form.parent_id = int(request.POST.get("parent"))
#             form.gift = gift
#             form.save()
#         return redirect(gift.get_absolute_url())
#
#
#
# def index(request):
#     return render(request, 'map.html')
