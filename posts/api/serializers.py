from rest_framework import serializers

from posts.models import Post, PostComment, PostView, PostReact


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["id", 'text', 'created', 'updated']


class PostReactSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostReact
        fields = ['id', 'user', 'post', 'react']
        read_only_fields = ['post', "user"]


class PostCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostComment
        fields = ['id', 'user', 'post', 'text']


class PostViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostView
        fields = ['id', 'user', 'post']
