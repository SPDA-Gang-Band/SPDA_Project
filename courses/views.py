from rest_framework import permissions, viewsets

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

from courses.models import CourseRequest
from courses.serializers import CourseRequestSerializer


class CourseRequestViewSet(viewsets.ModelViewSet):
    queryset = CourseRequest.objects.all()
    serializer_class = CourseRequestSerializer
    permissions = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['start_date', 'study_quarter', 'status']
    search_fields = ['name', 'surname', 'course_name', 'description']

    def get_serializer_context(self):
        return {'request': self.request}

    def get_queryset(self):
        if self.request.user.is_superuser:
            return CourseRequest.objects.all()
        else:
            return CourseRequest.objects.filter(user=self.request.user)
