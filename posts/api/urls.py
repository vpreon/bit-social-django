from django.urls import path, include
from rest_framework_nested import routers


from posts.api.views import PostViewSet, PostReactViewSet, PostCommentViewSet, PostViewViewSet

router = routers.SimpleRouter()
router.register(r'posts', PostViewSet)

posts_router = routers.NestedSimpleRouter(router, r'posts', lookup='post')
posts_router.register(r'reacts', PostReactViewSet, basename='post-reacts')
posts_router.register(r'comments', PostCommentViewSet, basename='post-comments')
posts_router.register(r'views', PostViewViewSet, basename='post-views')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(posts_router.urls))
]
