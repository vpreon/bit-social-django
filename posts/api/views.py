from django.db.models import Count, Exists, OuterRef

from rest_framework import viewsets, mixins, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from posts.api.serializers import MediaSerializer, PostSerializer, PostCommentSerializer, PostViewSerializer, PostReactSerializer
from posts.models import Media, Post, PostReact, PostComment, PostView


class PostViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return self.queryset.prefetch_related('comments').annotate(
            reacts=Count('post_react'),
            reacted=Exists(PostReact.objects.filter(user=self.request.user, post=OuterRef('pk'))))


class PostReactViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = PostReactSerializer
    queryset = PostReact.objects.all()

    def create(self, request, *args, **kwargs):
        instance = self.queryset.filter(
            user=request.user, post=kwargs['post_pk']).first()

        if instance:
            if instance.react == request.data['react']:
                instance.delete()
                return Response({"message": "React deleted"}, status=status.HTTP_201_CREATED)
            else:
                instance.react = request.data['react']
                instance.save()
                serializer = PostReactSerializer(instance)
                return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(user=request.user, post_id=kwargs['post_pk'])
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class PostCommentViewSet(viewsets.ModelViewSet):
    serializer_class = PostCommentSerializer
    queryset = PostComment.objects.all()

    def get_queryset(self):
        return self.queryset.filter(post=self.kwargs.get('post_pk'))
    
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user, post_id=self.kwargs.get('post_pk'))


class PostViewViewSet(viewsets.ModelViewSet):
    serializer_class = PostViewSerializer
    queryset = PostView.objects.all()

    def get_queryset(self):
        return self.queryset.filter(post=self.kwargs.get('post_pk'))


class MediaViewSet(viewsets.ModelViewSet):
    serializer_class = MediaSerializer
    queryset = Media.objects.all()
    
    
    def get_queryset(self):
        return self.queryset.filter(post=self.kwargs.get('post_pk'))
    
    def perform_create(self, serializer):
        serializer.save(post_id=self.kwargs.get('post_pk'))


    
    
    