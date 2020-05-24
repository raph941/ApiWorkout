from django.db import models
from accounts.models import User


class Articles(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField( max_length=350)
    description = models.CharField( max_length= 1000)


class Comments(models.Model):
    articles = models.ForeignKey(Articles, related_name="article_comments", on_delete=models.CASCADE)
    comment_author = models.ForeignKey(User, related_name="my_comments", on_delete=models.CASCADE)
    content = models.CharField(max_length=250)