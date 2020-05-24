from django.conf.urls import url
from .views import ArticlesRUDView, ArticleListView, CommentsCreateView


urlpatterns = [
    url(r"^$", ArticleListView.as_view(), name="articles_list"),
    url(r"^(?P<pk>\d+)$", ArticlesRUDView.as_view(), name="articles"),
    url(r"^comment/(?P<article>\d+)$", CommentsCreateView.as_view(), name="article_comment"),
]