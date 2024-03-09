from django.urls import path
from . import views

urlpatterns = [
    path("hello/", views.Index.as_view(), name="index"),
    path('courses/', views.course_list, name='course_list'),
    path('courses/<int:course_id>/', views.course_detail, name='course_detail'),
    path('courses/<int:course_id>/enroll/', views.enroll_in_course, name='enroll_in_course'),
]
