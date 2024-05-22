from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework import viewsets

from .mixins import IsAuthorMixin
from posts.models import Comment, Post, Group
from .serializers import CommentSerializer, GroupSerializer, PostSerializer


class PostViewSet(IsAuthorMixin, viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(IsAuthorMixin, viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        post = get_object_or_404(Post, id=self.kwargs['post_id'])
        serializer.save(author=self.request.user, post=post)

    def get_queryset(self):
        post_id = self.kwargs.get('post_id')
        post = get_object_or_404(Post, id=post_id)
        return Comment.objects.filter(post=post)


class GroupViewSet(ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
