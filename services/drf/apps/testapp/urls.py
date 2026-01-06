"""Docstring for services.backend.apps.testapp.urls."""

from django.urls import path  # noqa: F401
from rest_framework.routers import DefaultRouter

from apps.testapp.views import ProjectList

router = DefaultRouter()
router.register(r"project", ProjectList, basename="project")

urlpatterns = []
urlpatterns += router.urls
