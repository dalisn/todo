from django.urls import path
from accounts import views

app_name = "auth"  # Namespace for the auth app

urlpatterns = [
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("register/", views.register, name="register"),
]
