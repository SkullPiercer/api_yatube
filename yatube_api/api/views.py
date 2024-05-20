from rest_framework.viewsets import ReadOnlyModelViewSet

from posts.models import Post, Comment, Group
from .mixins import ListCreateMixin
from .serializers import PostSerializer, GroupSerializer


class PostViewSet(ListCreateMixin):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class GroupViewSet(ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
