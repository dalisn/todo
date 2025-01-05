from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView  # Import RedirectView

urlpatterns = [
    # Redirect the root URL to the login page
    path('', RedirectView.as_view(url='/auth/login/', permanent=False)),  # This will redirect to /auth/login/

    path("admin/", admin.site.urls),
    path("auth/", include("accounts.urls")),  # Login and auth-related paths
    path("", include("lists.urls")),  # The "lists" app
    path("api/", include("api.urls")),
    path("api-auth/", include("rest_framework.urls")),
]
