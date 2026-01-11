"""Docstring for services.backend.apps.testapp.views."""

from django.db.models import Count, Prefetch
from rest_framework import viewsets

from apps.testapp.models import Comment, Project

from .serializers import ProjectSerializer


class ProjectList(viewsets.ModelViewSet):
    """Docstring for ProjectList."""

    queryset = (
        Project.objects.select_related("owner")
        .prefetch_related(
            Prefetch("comments", queryset=Comment.objects.select_related("owner"))
        )
        .annotate(comments_count=Count("comments"))
    )
    serializer_class = ProjectSerializer
