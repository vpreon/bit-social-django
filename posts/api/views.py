from rest_framework import viewsets

from posts.api.serializers import PostSerializer, PostCommentSerializer, PostViewSerializer, PostReactSerializer
from posts.models import Post, PostReact, PostComment, PostView


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class PostReactViewSet(viewsets.ModelViewSet):
    serializer_class = PostReactSerializer
    queryset = PostReact.objects.all()

    def get_queryset(self):
        return self.queryset.filter(post=self.kwargs['post_pk'])


class PostCommentViewSet(viewsets.ModelViewSet):
    serializer_class = PostCommentSerializer
    queryset = PostComment.objects.all()

    def get_queryset(self):
        return self.queryset.filter(post=self.kwargs['post_pk'])


class PostViewViewSet(viewsets.ModelViewSet):
    serializer_class = PostViewSerializer
    queryset = PostView.objects.all()

    def get_queryset(self):
        return self.queryset.filter(post=self.kwargs['post_pk'])
