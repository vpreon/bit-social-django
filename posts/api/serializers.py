from rest_framework import serializers

from posts.models import Post, PostComment, PostView, PostReact


class PostSerializer(serializers.ModelSerializer):
    reacts = serializers.SerializerMethodField()
    reacted = serializers.SerializerMethodField()
    comments = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ["id", 'text', 'reacts', 'reacted',
                  'comments', 'created', 'updated']

    def get_reacts(self, obj):
        return obj.reacts

    def get_reacted(self, obj):
        return obj.reacted

    def get_comments(self, obj):
        serialized_comment = PostCommentSerializer(obj.comments, many=True)
        return serialized_comment.data
        return 1


class PostReactSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostReact
        fields = ['id', 'user', 'post', 'react']
        read_only_fields = ['post', "user"]


class PostCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostComment
        fields = ['id', 'user', 'post', 'text']
        read_only_fields = ['user', 'post']


class PostViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostView
        fields = ['id', 'user', 'post']
