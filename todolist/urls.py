from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("auth/", include("accounts.urls")),  # Login and auth-related paths
    path("", include("lists.urls")),  # The "lists" app, set as the default
    path("api/", include("api.urls")),
    path("api-auth/", include("rest_framework.urls")),
]
