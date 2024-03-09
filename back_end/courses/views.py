from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Course


def course_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/course_list.html', {'courses': courses})


def course_detail(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    return render(request, 'courses/course_detail.html', {'course': course})


def enroll_in_course(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    # Logic to enroll the user in the course
    # ...
    return render(request, 'courses/enroll_success.html', {'course': course})


class Index(APIView):
    def get(self, request, format=None):
        return Response('Hello World!')
