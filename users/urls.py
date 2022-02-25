from django.urls import path
from . import views


app_name='users'
urlpatterns = [
    path("login/", views.LoginProfile.as_view(), name='login'),
    path("logout/", views.LogoutProfile.as_view(), name='logout'),
    path("signup/", views.signup, name='signup'),
    path("me/profile/", views.update_profile, name='update_profile'),
]
