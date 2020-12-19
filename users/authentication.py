from rest_framework import authentication

from .exceptions import NoAuthToken, InvalidAuthToken
from users.models import User


class LoginAuthentication(authentication.BaseAuthentication):

    def authenticate_header(self, request):
        return 'fullname'

    def authenticate(self, request):
        auth_header = request.META.get("HTTP_AUTHORIZATION")

        if not auth_header:
            raise NoAuthToken("No auth token provided")

        name, surname = auth_header.split(" ")[1:3]
        if name is None or surname is None or name == '' or surname == '':
            raise InvalidAuthToken("Name or surname is empty")
        user, created = User.objects.get_or_create(first_name=name, last_name=surname)

        return (user, f'{name} {surname}')
