"""Docstring for services.backend.apps.testapp.factories."""

import factory  # noqa: I001
from django.contrib.auth.models import User
# from faker import Faker  # noqa: ERA001

from apps.testapp.models import Project

# fake = Faker("ru_RU")  # noqa: ERA001


class ProjectFactory(factory.django.DjangoModelFactory):
    """Docstring for ProjectFactory."""

    class Meta:
        """Docstring for Meta."""

        model = Project

    title = factory.Faker("text", locale="ru_RU", max_nb_chars=100)
    description = factory.Faker("text", locale="ru_RU", max_nb_chars=500)
    owner = factory.LazyFunction(lambda: User.objects.get(id=1))
