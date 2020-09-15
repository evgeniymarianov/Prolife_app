from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.base import View
from django.http import HttpResponse, JsonResponse, Http404
from rest_framework.parsers import JSONParser
from gifts.serializers import GiftSerializer
from rest_framework import mixins
from rest_framework import generics

from .models import Gift, Category
from .forms import CommentForm


class GiftList(mixins.ListModelMixin,
               mixins.CreateModelMixin,
               generics.GenericAPIView):
    """
    List all code gifts, or create a new gift.
    """
    queryset = Gift.objects.all()
    serializer_class = GiftSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class GiftDetail(mixins.RetrieveModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.DestroyModelMixin,
                 generics.GenericAPIView):
    """
    Retrieve, update or delete a code gift.
    """
    queryset = Gift.objects.all()
    serializer_class = GiftSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


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
