"""Docstring для services.backend.apps.testapp.models.tag."""

from typing import Any

from django.db import models
from django.utils.text import slugify


class Tag(models.Model):
    """Docstring для Tag."""

    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(unique=True)

    def __str__(self) -> str:
        """Docstring для __str__.

        :param self: Описание.
        """
        return self.name

    def save(self, *args: list[Any], **kwargs: dict[Any:Any]) -> None:
        """Docstring для save.

        :param self: Описание
        :param args: Описание
        :type args: list[Any]
        :param kwargs: Описание
        :type kwargs: dict[Any: Any]
        """
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
