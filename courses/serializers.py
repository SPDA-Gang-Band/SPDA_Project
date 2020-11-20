from rest_framework import serializers

from courses.models import CourseRequest


class CourseRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseRequest
        fields = '__all__'
