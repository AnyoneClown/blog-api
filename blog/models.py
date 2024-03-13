import os
import uuid

from django.contrib.auth import get_user_model
from django.db import models
from django.utils.text import slugify


def image_file_path(instance, filename):
    _, extension = os.path.splitext(filename)
    filename = f"{slugify(instance)}-{uuid.uuid4()}{extension}"
    path = os.path.join("uploads", "posts")
    return os.path.join(path, filename)


class Post(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="posts")
    title = models.CharField(max_length=50)
    content = models.TextField()
    image = models.ImageField(upload_to=image_file_path, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["user"]
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        app_label = "blog"
        db_table = "posts"

    def __str__(self) -> str:
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="comments")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["user"]
        verbose_name = "Comment"
        verbose_name_plural = "Comments"
        app_label = "blog"
        db_table = "comments"

    def __str__(self) -> str:
        return f"Comment by {self.user} on {self.post.title}"
