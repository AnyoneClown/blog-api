from rest_framework import routers

from blog.views import PostViewSet, CommentViewSet

router = routers.DefaultRouter()
router.register("posts", PostViewSet)
router.register("comments", CommentViewSet)

urlpatterns = router.urls

app_name = "blog"
