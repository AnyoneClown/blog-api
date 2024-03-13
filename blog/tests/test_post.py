from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APIClient

from blog.models import Post, Comment
from blog.serializers import PostSerializer, CommentAddSerializer, CommentSerializer


class TestModels(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(email="testuser@gmail.com", password="testpassword")
        self.client.force_authenticate(user=self.user)

    def test_post_creation(self):
        post = Post.objects.create(user=self.user, title="Test Post", content="Test Content")
        self.assertEqual(Post.objects.count(), 1)
        self.assertEqual(post.title, "Test Post")

    def test_comment_creation(self):
        post = Post.objects.create(user=self.user, title="Test Post", content="Test Content")
        comment = Comment.objects.create(user=self.user, post=post, content="Test Comment")
        self.assertEqual(Comment.objects.count(), 1)
        self.assertEqual(comment.content, "Test Comment")

    def test_add_comment_and_create_post(self):
        post = Post.objects.create(user=self.user, title="Test Post", content="Test Content")

        post_serializer = PostSerializer(instance=post)

        expected_data = {
            "id": post.id,
            "user": self.user.id,
            "title": "Test Post",
            "content": "Test Content",
            "image": None,
            "created_at": post.created_at.strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
        }
        self.assertEqual(post_serializer.data, expected_data)

        comment_data = {"content": "Test comment content"}
        comment_serializer = CommentAddSerializer(data=comment_data)
        comment_serializer.is_valid()
        comment_serializer.save(user=self.user, post=post)
        self.assertEqual(post.comments.count(), 1)

        comment = Comment.objects.last()
        comment_serializer = CommentSerializer(instance=comment)

        expected_comment_data = {
            "id": comment.id,
            "user": self.user.id,
            "post": post.id,
            "content": "Test comment content",
            "created_at": comment.created_at.strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
        }
        self.assertEqual(comment_serializer.data, expected_comment_data)
