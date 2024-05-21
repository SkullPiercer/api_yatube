from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework import viewsets, status

from rest_framework.response import Response

from .mixins import IsAuthorMixin
from posts.models import Post, Comment, Group
from .serializers import CommentSerializer, PostSerializer, GroupSerializer


class PostViewSet(IsAuthorMixin, viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(IsAuthorMixin, viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, post=self.kwargs['post_id'])

    def list(self, request, *args, **kwargs):
        post_id = kwargs.get('post_id')
        queryset = self.queryset.filter(post_id=post_id)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class GroupViewSet(ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
