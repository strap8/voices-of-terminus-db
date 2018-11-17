from rest_framework import serializers
from articles.models import Article, ArticleComment
from django.contrib.auth.models import User

class ArticleSerializer(serializers.ModelSerializer):
    # author_name = serializers.StringRelatedField(source='documentAuthorName')
    #author_name = serializers.StringRelatedField(many=True)
    class Meta:
        model = Article
        fields = ('id','title', 'slug', 'author', 'author_username', 'html', 'tags',
        'date_created','last_modified', 'last_modified_by', 'last_modified_by_username', 'views'
        )
        read_only_fields = ('date_created', 'date_modified, last_modified,last_modified_by')

class CommentSerializer(serializers.ModelSerializer):
    # author_name = serializers.StringRelatedField(source='documentAuthorName')
    #author_name = serializers.StringRelatedField(many=True)
    class Meta:
        model = ArticleComment
        fields = ('id','article', 'author', 'author_username', 'text',
        'date_created','last_modified', 'last_modified_by', 'last_modified_by_username', 'likes'
        )
        read_only_fields = ('date_created', 'date_modified, last_modified,last_modified_by')