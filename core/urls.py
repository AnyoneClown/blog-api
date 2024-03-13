from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from core import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/users/", include("user.urls", namespace="user")),
    path("api/blog/", include("blog.urls", namespace="blog")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
