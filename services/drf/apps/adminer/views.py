"""Docstring для services.drf.apps.adminer.views."""

from django.http import HttpRequest, HttpResponse
from django.views import View
from rest_framework import status


class ProtectedAdminerView(View):
    """Docstring для ProtectedAdminerView."""

    def get(self, request: HttpRequest) -> HttpResponse:
        """Docstring для get.

        :param self: Описание
        :param request: Описание
        :type request: HttpRequest
        :return: Описание
        :rtype: HttpResponse
        """
        if request.user.is_authenticated and request.user.is_staff:
            return HttpResponse(status=status.HTTP_200_OK)

        return HttpResponse(status=status.HTTP_401_UNAUTHORIZED)
