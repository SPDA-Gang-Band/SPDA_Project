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
    permissions = [permissions.IsAuthenticated]

    def get_serializer_context(self):
        return {'request': self.request}

    def get_queryset(self):
        if self.request.user.is_superuser:
            return CourseRequest.objects.all()
        else:
            return CourseRequest.objects.filter(user=self.request.user)