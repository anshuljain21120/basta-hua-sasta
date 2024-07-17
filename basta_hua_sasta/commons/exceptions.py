from rest_framework import status
from rest_framework.exceptions import APIException


class UserNotLoggedIn(APIException):
    status_code = status.HTTP_401_UNAUTHORIZED
    default_detail = 'User not logged in'
    default_code = 'unauthorized_user'
