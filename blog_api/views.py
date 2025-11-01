from django.core.serializers import serialize
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics, permissions

from blog.models import Post
from .serializers import PostSerializer
from django_filters.rest_framework import DjangoFilterBackend
from .permissions import IsAuthorOrReadOnly


class PostList(generics.ListCreateAPIView):
    permission_classes = (IsAuthorOrReadOnly, )
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['author']


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly, )
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class UserPostList(generics.ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        user = self.kwargs['id']
        return Post.objects.filter(author=user)

    '''
    def get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = PostSerializer(post, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        post = self.get_object(pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    '''