from django.shortcuts import render
from .models import Case
from django.views.generic import ListView, DetailView, CreateView


# def home(request):
    # list_cases = Case.objects.all()
    # context = {    'list_cases': list_cases}
    # template = 'index.html'
    # return render(request, template, context)
class CasesView(ListView):
    """Список фильмов"""
    model = Case
    queryset = Case.objects.all()
    #template_name = "movies/movies.html"


class HomeDetailView(DetailView):
    model = Case
    template_name = 'detail.html'
    context_object_name = 'get_case'
