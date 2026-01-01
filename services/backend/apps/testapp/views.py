"""Docstring for services.backend.apps.testapp.views."""

from django.db.models import Count
from rest_framework import generics

from apps.testapp.models import Project

from .serializers import ProjectSerializer


class ProjectList(generics.ListCreateAPIView):
    """Docstring for ProjectList."""

    # queryset = Project.objects.prefetch_related("comments").all()  # noqa: ERA001
    queryset = Project.objects.annotate(comments_count=Count("comments")).all()
    serializer_class = ProjectSerializer
