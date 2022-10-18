from django.urls import path, include
from rest_framework import routers

from .views import CommentVewSet, GroupViewSet, PostViewSet, FollowViewSet

router = routers.DefaultRouter()
router.register(
    r'posts/(?P<post_id>\d+)/comments', CommentVewSet, basename='comment'
)
router.register(r'groups', GroupViewSet)
router.register(r'posts', PostViewSet)
router.register(r'follow', FollowViewSet)

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/', include('djoser.urls.jwt')),
]
