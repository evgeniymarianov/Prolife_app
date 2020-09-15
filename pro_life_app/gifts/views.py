from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.base import View
from django.http import HttpResponse, JsonResponse, Http404
from rest_framework.parsers import JSONParser
from gifts.serializers import GiftListSerializer, CommentCreateSerializer
from rest_framework import mixins
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Gift, Category
from .forms import CommentForm


class GiftList(generics.ListCreateAPIView):
    """
    List all code gifts, or create a new gift.
    """
    queryset = Gift.objects.all()
    serializer_class = GiftListSerializer


class GiftDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a code gift.
    """
    queryset = Gift.objects.all()
    serializer_class = GiftListSerializer


class CommentCreateView(APIView):
    """Добавление отзыва к фильму"""
    def post(self, request):
        comment = CommentCreateSerializer(data=request.data)
        if comment.is_valid():
            comment.save()
        return Response(status=201)


class GiftsView(ListView):
    """Список Даров"""
    model = Gift
    queryset = Gift.objects.all()


class GiftDetailView(DetailView):
    """Полное описание Дара"""
    model = Gift
    slug_field = "url"


class AddComment(View):
    """Отзыв"""
    def post(self, request, pk):
        form = CommentForm(request.POST)
        gift = Gift.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get("parent", None):
                form.parent_id = int(request.POST.get("parent"))
            form.gift = gift
            form.save()
        return redirect(gift.get_absolute_url())



def index(request):
    return render(request, 'map.html')
