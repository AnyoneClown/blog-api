from rest_framework import serializers

from blog.models import Comment, Post


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["id", "user", "post", "content", "created_at"]


class CommentPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ["id", "content", "created_at"]


class CommentAddSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ["id", "content"]


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"


class PostListSerializer(serializers.ModelSerializer):
    comments = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ["id", "user", "title", "content", "image", "created_at", "comments"]

    @staticmethod
    def get_comments(obj):
        comments = Comment.objects.filter(post=obj)
        serializer = CommentPostSerializer(comments, many=True)
        return serializer.data
