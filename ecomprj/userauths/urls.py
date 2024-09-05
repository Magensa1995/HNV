from django.urls import path
from userauths.views import register_view, login_view, logout_view, home_view

app_name = "userauths"
urlpatterns = [
    path("register/", register_view, name="register"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("", home_view, name="home"),
]
