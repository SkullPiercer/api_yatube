from rest_framework import mixins, viewsets
from posts.models import Post, Comment, Group
from .serializers import PostSerializer


class ListCreateMixin(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    pass


class PostViewSet(ListCreateMixin):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
