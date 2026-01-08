"""Docstring для services.drf.apps.auth_check.views."""

from django.http import HttpRequest, HttpResponse
from django.views import View
from rest_framework import status


class ProtectedUrlView(View):
    """Docstring для ProtectedUrlView."""

    def check_url(self, request: HttpRequest) -> bool:
        """Проверка url.

        :param request: _description_
        :type request: HttpRequest
        :return: _description_
        :rtype: bool
        """
        protected_urls = [
            "/adminer",
            "/jupyter",
            "/sphinx",
            "/django-api-swagger",
            "/django-api-redoc",
            "/django-api-schema",
        ]
        original_uri = request.headers.get("X-Original-URI")
        return original_uri.startswith(tuple(protected_urls))

    def get(self, request: HttpRequest) -> HttpResponse:
        """Docstring для get.

        :param self: Описание
        :param request: Описание
        :type request: HttpRequest
        :return: Описание
        :rtype: HttpResponse
        """
        # TODO Добавить проверку по группам
        if self.check_url(request) and request.user.is_authenticated:
            return HttpResponse(status=status.HTTP_200_OK)
        return HttpResponse(status=status.HTTP_401_UNAUTHORIZED)
