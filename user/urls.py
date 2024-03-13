from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from user.views import UserView

user_urlpatterns = [
    path("", UserView.as_view({"get": "list", "post": "create"}), name="user-list-create"),
    path(
        "<int:pk>/",
        UserView.as_view({"get": "retrieve", "put": "update", "patch": "partial_update", "delete": "destroy"}),
        name="user-detail",
    ),
]

token_urlpatterns = [
    path("token/", TokenObtainPairView.as_view(), name="token-obtain-pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token-refresh"),
    path("token/verify/", TokenVerifyView.as_view(), name="token-verify"),
]

urlpatterns = user_urlpatterns + token_urlpatterns

app_name = "users"
