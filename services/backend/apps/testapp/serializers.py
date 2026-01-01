"""Docstring for services.backend.apps.testapp.serializers."""

from rest_framework import serializers

from apps.testapp.models import Comment, Project


class CommentSerializer(serializers.ModelSerializer):
    """Docstring для CommentSerializer."""

    class Meta:
        """Docstring для Meta."""

        model = Comment
        fields = [  # noqa: RUF012
            "id",
            "title",
            "description",
            "project",
            "owner",
            "created_at",
            "updated_at",
        ]


class ProjectSerializer(serializers.ModelSerializer):
    """Docstring for ProjectSerializer."""

    # comments = CommentSerializer(many=True, read_only=True)  # noqa: ERA001
    comments_count = serializers.IntegerField(read_only=True)

    class Meta:
        """Docstring for Meta."""

        model = Project
        fields = ["id", "title", "description", "owner", "comments_count"]  # noqa: RUF012
