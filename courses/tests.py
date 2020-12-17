import requests
from django.test import TestCase, override_settings

# Create your tests here.
from rest_framework.test import APIRequestFactory

from courses.views import CourseRequestViewSet


class CourseRequestsMethodsTest(TestCase):
    def setUp(self):
        self.login = "TestUser"

    @override_settings(DEBUG=True)
    def test_post_course_request(self):
        factory = APIRequestFactory()
        request = factory.post('', format='json', HTTP_AUTHORIZATION=f"login {self.login}", data={
            "surname": "TestSur",
            "name": "TestName",
            "course_name": "new course",
            "link": "testlink.ru",
            "price": "42$",
            "start_date": "string",
            "study_quarter": 4,
            "description": "Very interesting",
        })
        response = CourseRequestViewSet.as_view({'post': 'create'})(request)
        if response.status_code != 201:
            print('DATA  : ', response.data)
            print('CODE  : ', response.status_code)
        self.assertTrue(response.status_code == 201)
