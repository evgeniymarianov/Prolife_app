from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.base import View

from .models import Gift, Category
from .forms import CommentForm

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
