from posts.models import Post, Comment, Group

from .mixins import ListCreateMixin
from .serializers import PostSerializer


class PostViewSet(ListCreateMixin):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
