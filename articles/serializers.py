from rest_framework import serializers
from articles.models import Article, ArticleLikes, ArticleComment
from django.contrib.auth.models import User


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'slug', 'author', 'author_username', 'html', 'tags',
                  'date_created', 'last_modified', 'last_modified_by', 'last_modified_by_username', 'views'
                  )
        read_only_fields = (
            'date_created', 'date_modified, last_modified,last_modified_by')


class ArticleNoHtmlSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'slug', 'author', 'author_username', 'tags',
                  'date_created', 'last_modified', 'last_modified_by', 'last_modified_by_username', 'views',)
        read_only_fields = (
            'date_created', 'date_modified, last_modified,last_modified_by')


class ArticleHtmlSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'html',)


class ArticleLikesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleLikes
        fields = ('id', 'document_id', 'author',
                  'author_username', 'count', 'date_created',)
        read_only_fields = ('date_created',)


class ArticleCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleComment
        fields = ('id', 'document_id', 'author', 'author_username', 'author_profile_image', 'text',
                  'date_created', 'last_modified', 'last_modified_by', 'last_modified_by_username', 'likes'
                  )
        read_only_fields = (
            'date_created', 'date_modified, last_modified,last_modified_by')
