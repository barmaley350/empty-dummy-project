"""Docstring для services.drf.apps.adminer.models."""

from typing import ClassVar

from django.db import models


class AdminerPermission(models.Model):
    """Docstring для AdminerPermission."""

    class Meta:
        """Docstring для Meta."""

        permissions: ClassVar[dict] = [
            ("view_adminer", "Может просматривать adminer"),
        ]

    def __str__(self) -> str:
        """Docstring for __str__.

        :param self: Description
        :return: Description
        :rtype: str
        """
        return "AdminerPermission"
