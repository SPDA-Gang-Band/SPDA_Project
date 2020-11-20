from rest_framework import permissions, viewsets

from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import action
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import SAFE_METHODS

from courses.models import CourseRequest
from courses.serializers import CourseRequestSerializer


class CourseRequestViewSet(viewsets.ModelViewSet):
    queryset = CourseRequest.objects.all()
    serializer_class = CourseRequestSerializer
    permissions = [permissions.AllowAny]