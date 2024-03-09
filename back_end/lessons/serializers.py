from django.contrib.auth import get_user_model
from django.db.models import Sum
from rest_framework import serializers

from .models import Product, Lesson, LessonAccess

User = get_user_model()


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'owner')


class LessonSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Lesson
        fields = ('id', 'title', 'video_link', 'duration', 'products')


class LessonWithAccessSerializer(LessonSerializer):
    status = serializers.SerializerMethodField()
    viewed_time = serializers.SerializerMethodField()

    class Meta(LessonSerializer.Meta):
        fields = LessonSerializer.Meta.fields + ('status', 'viewed_time')

    def _get_lesson_access(self, obj):
        user = self.context['request'].user

        return LessonAccess.objects.filter(
            user=user, lesson=obj
        ).first()

    def get_status(self, obj):
        lesson_access = self._get_lesson_access(obj)
        return 'Просмотрен' if lesson_access.viewed else 'Не просмотрен'

    def get_viewed_time(self, obj):
        lesson_access = self._get_lesson_access(obj)
        return lesson_access.viewed_time


class ProductLessonSerializer(LessonWithAccessSerializer):

    last_viewed = serializers.SerializerMethodField()

    class Meta(LessonWithAccessSerializer.Meta):
        fields = (
            'id', 'title', 'video_link', 'duration', 'status',
            'viewed_time', 'last_viewed'
        )

    def get_last_viewed(self, obj):
        lesson_access = self._get_lesson_access(obj)
        return lesson_access.last_viewed_date


class ProductStatisticsSerializer(serializers.ModelSerializer):

    total_lessons_watched = serializers.SerializerMethodField()
    total_time_spent = serializers.SerializerMethodField()
    students_engaged = serializers.SerializerMethodField()
    product_acquisition_percentage = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = (
            'id', 'total_lessons_watched', 'total_time_spent',
            'students_engaged', 'product_acquisition_percentage'
        )

    @staticmethod
    def get_total_lessons_watched(obj):
        return LessonAccess.objects.filter(
            lesson__products=obj, viewed=True
        ).count()

    @staticmethod
    def get_total_time_spent(obj):

        result = LessonAccess.objects.filter(
            lesson__products=obj
        ).aggregate(total_time=Sum('viewed_time'))

        return result['total_time'] or 0

    @staticmethod
    def get_students_engaged(obj):
        return LessonAccess.objects.filter(
            lesson__products=obj
        ).values('user').distinct().count()

    def get_product_acquisition_percentage(self, obj):
        total_users = User.objects.count()
        students_engaged = self.get_students_engaged(obj)
        return (students_engaged / total_users) * 100 if total_users > 0 else 0
