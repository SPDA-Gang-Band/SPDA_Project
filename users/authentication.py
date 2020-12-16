from rest_framework import authentication

from .exceptions import NoAuthToken, InvalidAuthToken
from users.models import User


class LoginAuthentication(authentication.BaseAuthentication):

    def authenticate_header(self, request):
        return 'login'

    def authenticate(self, request):
        auth_header = request.META.get("HTTP_AUTHORIZATION")

        if not auth_header:
            raise NoAuthToken("No auth token provided")

        login = auth_header.split(" ").pop()
        if login is None or login == '':
            raise InvalidAuthToken("Login is empty")
        user, created = User.objects.get_or_create(username=login)

        return (user, login)
