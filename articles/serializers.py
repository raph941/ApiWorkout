from articles.models import Articles, Comments
from rest_framework import serializers

from django_restql.mixins import DynamicFieldsMixin
from django_restql.serializers import NestedModelSerializer 
from django_restql.fields import NestedField


class ArticleCommentSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = '__all__'


class ArticleSerializer(DynamicFieldsMixin, NestedModelSerializer):
    article_comments = NestedField(ArticleCommentSerializer, many=True, exclude = ['id'], required=False)

    class Meta:
        model = Articles
        fields = ['id', 'author', 'title', 'description', 'article_comments']