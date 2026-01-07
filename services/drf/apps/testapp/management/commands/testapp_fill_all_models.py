"""Docstring для services.backend.apps.testapp.management.commands.testapp_fill_all_models."""  # noqa: E501

import random
from typing import Any

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandParser

from apps.testapp.factories import (
    CommentFactory,
    ProjectFactory,
    TagFactory,
    UserFactory,
)
from apps.testapp.models import Comment, Project, Tag


class Command(BaseCommand):
    """Docstring for Command."""

    help = "Заполнение моделей приложения apps/testapp фейковыми данными"

    def add_arguments(self, parser: CommandParser) -> None:
        """Docstring для add_arguments.

        :param parser: Описание
        :type parser: CommandParser
        """
        parser.add_argument(
            "--clear",
            action="store_true",
            help="Очисть все данные перед заполнением (default=False)",
        )

        parser.add_argument(
            "--count",
            type=int,
            default=100,
            help="Количество записей для создания (default=100)",
        )

    def print_stat(self) -> None:
        """Вывод статистики."""
        projects = Project.objects.count()
        tags = Tag.objects.count()
        comments = Comment.objects.count()
        users = User.objects.count()

        self.output_text("")
        self.output_text(f"Кол-во проектов {projects}")
        self.output_text(f"Кол-во тегов {tags}")
        self.output_text(f"Кол-во коментариев {comments}")
        self.output_text(f"Кол-во пользователей {users}")

    def clear_data(self, **options: dict[str:Any]) -> None:
        """Docstring для clear_data.

        :param option: Описание
        :type option: dict[str: Any]
        """
        if options.get("clear"):
            Project.objects.all().delete()
            Tag.objects.all().delete()
            User.objects.filter(pk__gt=1).delete()

    def output_text(self, text: str, output_type: str = "success") -> None:
        """Вывод текства в консоль.

        :param text: Текст для вывода
        :type text: str
        :param output_type: Тип вывода, defaults to "success"
        :type output_type: str, optional
        """
        match output_type:
            case "seccuss":
                self.stdout.write(self.style.SUCCESS(text))
            case "error":
                self.stdout.write(self.style.ERROR(text))
            case _:
                self.stdout.write(self.style.SUCCESS(text))

    def output_process(self) -> None:
        """Docstring для output_process."""
        print(".", end="")  # noqa: T201

    def filling_project_models(self, **options: dict[str:Any]) -> None:
        """Заполнение моделей данными.

        :return: _description_
        :rtype: None
        """
        count = options.get("count")

        self.clear_data(**options)

        projects = ProjectFactory.create_batch(count)
        tags = TagFactory.create_batch(10)
        users = UserFactory.create_batch(10)

        for project in projects:
            project_author = random.choice(users)  # noqa: S311
            project.owner = project_author
            project.save()

            project.tags.add(*random.choices(tags, k=random.randint(3, 6)))  # noqa: S311
            # CommentFactory.create_batch(random.randint(5, 20), project=project)  # noqa: E501, ERA001

            for _ in range(random.randint(5, 20)):  # noqa: S311
                CommentFactory.create(project=project, owner=random.choice(users))  # noqa: S311
            self.output_process()

    def handle(self, *args: list[Any], **options: dict[str:Any]) -> None:
        """Docstring для handle.

        :param self: Описание
        :param args: Описание
        :type args: list[Any]
        :param options: Описание
        :type options: dict[str: Any]
        """
        self.output_text(f"Создаем проекты - {options.get('count')} шт. Ожидайте...")
        self.filling_project_models(*args, **options)
        self.print_stat()
