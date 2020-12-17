from rest_framework import permissions, viewsets

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