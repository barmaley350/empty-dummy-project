"""Docstring для services.drf.apps.auth_check.urls."""

from django.urls import path

from apps.auth_check.views import ProtectedUrlView

urlpatterns = [
    path("", ProtectedUrlView.as_view(), name="protected-url"),
]
