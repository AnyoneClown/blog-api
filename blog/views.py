from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from blog.models import Post, Comment
from blog.permissions import IsOwnerOrReadOnly
from blog.serializers import PostSerializer, PostListSerializer, CommentSerializer, CommentAddSerializer


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 25
    page_size_query_param = "page_size"
    max_page_size = 100


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.select_related("user")
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticated]
    pagination_class = StandardResultsSetPagination

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return PostListSerializer
        return self.serializer_class

    @action(
        detail=True,
        methods=["POST"],
        url_path="add-comment",
        permission_classes=[IsAuthenticated],
        serializer_class=CommentAddSerializer
    )
    def add_comment(self, request, pk=None):
        data = request.data.copy()

        serializer = CommentAddSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user, post=self.get_object())
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.select_related("user", "post")
    serializer_class = CommentSerializer
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticated]
