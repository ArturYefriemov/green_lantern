from django.urls import path
from django.views.generic import TemplateView
from apps.articles.views import main_page, SearchResultsView, ArticlesView, ArticlesListView, article_json,\
    articles_list_json


app_name = 'articles'

urlpatterns = [
    path('search/', main_page, name='main-page'),
    path('results/', SearchResultsView.as_view(), name='search-results'),
    path('articles/', ArticlesView.as_view(), name='articles_url'),
    path('articles_list/', ArticlesListView.as_view(), name='articles_list_url'),
    path('success/', TemplateView.as_view(template_name="pages/success.html"), name='success_url'),
    path('json/<int:id>', article_json, name='json'),
    path('json_list/', articles_list_json, name='json_list')
]
