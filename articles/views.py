from django.shortcuts import render
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListAPIView, ListCreateAPIView, CreateAPIView
from .serializers import ArticleSerializer, ArticleCommentSerializer
from rest_framework.permissions import AllowAny

from articles.models import Articles, Comments


class ArticlesRUDView(RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    queryset = Articles.objects.all()
    serializer_class = ArticleSerializer

   
class ArticleListView(ListCreateAPIView):
    serializer_class = ArticleSerializer
    queryset = Articles.objects.all()


class CommentsCreateView(CreateAPIView):
    lookup_field = 'article'
    queryset = Comments.objects.all()
    serializer_class = ArticleCommentSerializer