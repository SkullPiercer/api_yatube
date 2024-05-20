from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from posts.models import Post, Comment, Group
from .mixins import ListCreateMixin
from .serializers import PostSerializer, GroupSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
