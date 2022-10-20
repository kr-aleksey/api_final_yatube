from django.shortcuts import get_object_or_404
from rest_framework import viewsets, permissions
from rest_framework.filters import SearchFilter
from rest_framework.pagination import LimitOffsetPagination

from posts.models import Group, Post, Follow
from . import serializers
from .permissions import IsAuthorOrReadOnly


class CommentVewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CommentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsAuthorOrReadOnly)

    def get_post(self):
        post_id = self.kwargs['post_id']
        return get_object_or_404(Post, pk=post_id)

    def get_queryset(self):
        post = self.get_post()
        return post.comments.select_related('author')

    def perform_create(self, serializer):
        post = self.get_post()
        serializer.save(author=self.request.user, post=post)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = serializers.GroupSerializer
    permission_classes = (permissions.AllowAny,)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.select_related('author')
    serializer_class = serializers.PostSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsAuthorOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class FollowViewSet(viewsets.ModelViewSet):
    queryset = Follow.objects.all()
    serializer_class = serializers.FollowSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (SearchFilter,)
    search_fields = ('following__username',)

    def get_queryset(self):
        queryset = self.queryset.select_related('user', 'following')
        return queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
