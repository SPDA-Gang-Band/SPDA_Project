from rest_framework import serializers

from courses.models import CourseRequest


class CourseRequestSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super(CourseRequestSerializer, self).create(validated_data)

    class Meta:
        model = CourseRequest
        extra_kwargs = {"user": {"read_only": True}}
        fields = '__all__'
