"""Docstring for services.backend.apps.sphinx_docs.urls."""

from django.urls import path

from apps.sphinx_docs.views import SphinxView

urlpatterns = [
    path("<path:path>", SphinxView.as_view(), name="sphinx_docs"),
    path("", SphinxView.as_view(), name="sphinx_docs_root"),
]
