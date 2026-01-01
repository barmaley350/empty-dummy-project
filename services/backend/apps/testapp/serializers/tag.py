"""Docstring для services.backend.apps.testapp.serializers.tag."""

from rest_framework import serializers

from apps.testapp.models import Tag


class TagSerializer(serializers.ModelSerializer):
    """Docstring для TagSerializer."""

    class Meta:
        """Docstring для Meta."""

        model = Tag
        fields = ["id", "name", "slug"]  # noqa: RUF012
