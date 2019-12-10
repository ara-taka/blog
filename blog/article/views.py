from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import ListView
from django.views.generic import DetailView
from .models import Article

# Create your views here.
class IndexView(TemplateView):

    template_name = 'article/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_articles'] = Article.objects.order_by('-create_date')[:3]
        return context


class ArticleListView(ListView):

    queryset = Article.objects.order_by('-create_date')


class ArticleDetailView(DetailView):

    model = Article