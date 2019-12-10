from django.urls import path

from . import views
from .views import IndexView

app_name = 'article'

urlpatterns = [
    path('', IndexView.as_view(), name = 'index'), 
    path('article/list', views.ArticleListView.as_view(), name = 'article_list'), 
    path('article/detail/<int:pk>/', views.ArticleDetailView.as_view(), name = 'article_detail')
]