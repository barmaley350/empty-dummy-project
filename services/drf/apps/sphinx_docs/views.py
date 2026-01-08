"""Docstring for services.backend.apps.testapp.views."""

from django.http import HttpRequest, HttpResponse
from django.views import View


class SphinxView(View):
    """Docstring for ProtectedSphinxView."""

    def get(self, request: HttpRequest, path: str = "") -> HttpResponse:  # noqa: ARG002
        """Docstring for get.

        :param self: Description
        :param request: Description
        :type request: HttpRequest
        :param path: Description
        :type path: str
        """
        response = HttpResponse()

        # При такое схеме работы есть ну удалять заголовки то будет два заголовка
        if "Content-Type" in response:
            del response["Content-Type"]

        response["X-Accel-Redirect"] = f"/internal/sphinx/{path}"
        return response
