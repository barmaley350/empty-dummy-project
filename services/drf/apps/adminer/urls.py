"""Docstring для services.drf.apps.adminer.urls."""

from django.urls import path

from apps.adminer.views import ProtectedAdminerView

urlpatterns = [
    path("", ProtectedAdminerView.as_view(), name="protected-adminer"),
]
