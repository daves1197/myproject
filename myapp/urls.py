from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("createseminar", views.create, name="create"),
    path("detailseminar/<str:seminar_id>", views.detail, name="detail"),
    path("part/<str:id>", views.part, name="part"),
    path("close/<str:id>", views.close, name="close"),
    path("mycourses", views.mycourses, name="mycourses")
 ]