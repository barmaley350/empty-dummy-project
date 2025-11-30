"""Docstring for services.backend.apps.testapp.views."""

from rest_framework import generics

from apps.testapp.models import Project

from .serializers import ProjectSerializer


class ProjectList(generics.ListCreateAPIView):
    """Docstring for ProjectList."""

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
