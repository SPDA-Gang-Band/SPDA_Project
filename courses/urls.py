from django.urls import path, include
from rest_framework.routers import SimpleRouter

from courses.views import CourseRequestViewSet

router = SimpleRouter()

router.register(r"course-requests", CourseRequestViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
