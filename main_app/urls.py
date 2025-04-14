"""Urls to views patterns"""
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("register/", views.register_view, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("my-score/", views.my_score, name="my_score"),
    path("add-cpp-example/", views.add_cpp_example, name="add_cpp_example"),
    path("cpp-explanations/", views.cpp_explanations, name="cpp_explanations"),
    path("cpp-quiz/", views.cpp_quiz, name="cpp_quiz"),
]
