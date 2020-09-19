from django.shortcuts import get_object_or_404
from rest_framework import viewsets, renderers, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Gift
from .serializers import (
    GiftListSerializer,
    GiftDetailSerializer,
)


class GiftViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Gift.objects.all()
        serializer = GiftListSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Gift.objects.all()
        gift = get_object_or_404(queryset, pk=pk)
        serializer = GiftDetailSerializer(actor)
        return Response(serializer.data)
