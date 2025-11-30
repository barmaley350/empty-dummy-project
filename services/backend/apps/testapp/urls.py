"""Docstring for services.backend.apps.testapp.urls."""

from django.urls import path

from apps.testapp.views import ProjectList

urlpatterns = [
    path("", ProjectList.as_view(), name="project-list"),
    path("project/", ProjectList.as_view(), name="project-list"),
]
