from rest_framework import serializers
from accounts.api.serializers import UserSerializer

from posts.models import Media, Post, PostComment, PostView, PostReact


class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = ['id', 'image']


class BasePostSerializer(serializers.ModelSerializer):
    reacts = serializers.SerializerMethodField()
    reacted = serializers.SerializerMethodField()
    comments = serializers.SerializerMethodField()
    medias = MediaSerializer(many=True, read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = Post
        fields = ["id", 'text', 'reacts', 'reacted',
                  'comments', 'post', 'medias', 'user', 'created', 'updated']

    def get_reacts(self, obj):
        if hasattr(obj, 'reacts'):
            return obj.reacts
        else:
            return []

    def get_reacted(self, obj):
        if hasattr(obj, 'reacted'):
            return obj.reacted
        return 0

    def get_comments(self, obj):
        serialized_comment = PostCommentSerializer(obj.comments, many=True)
        return serialized_comment.data


class ShareSerializer(BasePostSerializer):
    pass


class PostSerializer(BasePostSerializer):
    share = ShareSerializer(read_only=True, source='post')
    user = UserSerializer(read_only=True)

    class Meta:
        model = Post
        fields = BasePostSerializer.Meta.fields + \
            ['share', 'user', 'created', 'updated']

        extra_kwargs = {
            "post": {"write_only": True}
        }

    def validate(self, data):
        post = data.get('post')
        text = data.get('text')

        if not text and not post:
            raise serializers.ValidationError({'text': "Text is required."})

        return data


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
