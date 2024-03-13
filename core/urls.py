from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from core import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/users/", include("user.urls", namespace="user")),
    path("api/blog/", include("blog.urls", namespace="blog")),

    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/schema/swagger/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
