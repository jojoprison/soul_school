from django.contrib.auth import get_user_model
from rest_framework import viewsets, permissions

from .models import Product, Lesson, LessonAccess
from .serializers import LessonSerializer, ProductStatisticsSerializer, LessonWithAccessSerializer, \
    ProductLessonSerializer

User = get_user_model()


class LessonViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = LessonWithAccessSerializer

    def get_queryset(self):
        user = self.request.user
        return Lesson.objects.filter(lessonaccess__user=user)


class ProductLessonsViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ProductLessonSerializer

    def get_queryset(self):
        user = self.request.user
        product_id = self.kwargs['product_id']
        return Lesson.objects.filter(
            products__id=product_id, lessonaccess__user=user
        )


class ProductStatisticsViewSet(viewsets.ReadOnlyModelViewSet):

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ProductStatisticsSerializer

    def get_queryset(self):
        return Product.objects.all()
