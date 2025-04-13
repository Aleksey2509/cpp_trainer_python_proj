from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("add-cpp-example/", views.add_cpp_example, name="add_cpp_example"),
    path("cpp-explanations/", views.cpp_explanations, name="cpp_explanations"),
    path("cpp-quiz/", views.cpp_quiz, name="cpp_quiz"),
]
