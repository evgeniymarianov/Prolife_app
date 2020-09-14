from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.base import View
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from gifts.serializers import GiftSerializer
from rest_framework import status
from rest_framework.decorators import api_view


from .models import Gift, Category
from .forms import CommentForm


@api_view(['GET', 'POST'])
def gift_list(request):
    """
    List all code gifts, or create a new gift.
    """
    if request.method == 'GET':
        gifts = Gift.objects.all()
        serializer = GiftSerializer(gifts, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = GiftSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def gift_detail(request, pk):
    """
    Retrieve, update or delete a code gift.
    """
    try:
        gift = Gift.objects.get(pk=pk)
    except Gift.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = GiftSerializer(gift)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = GiftSerializer(gift, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        gift.delete()
        return HttpResponse(status=204)


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
