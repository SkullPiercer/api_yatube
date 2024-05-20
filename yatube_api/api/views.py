from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.serializers import GroupSerializer, PostSerializer
from posts.models import Group, Post


@api_view(['GET', 'POST'])
def get_posts(request):
    posts = Post.objects.all()
    if request.method == 'GET':
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = PostSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_groups(request):
    posts = Post.objects.all()
    if request.method == 'GET':
        serializer = GroupSerializer(posts, many=True)
        return Response(serializer.data)
