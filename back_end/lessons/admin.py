from django.contrib import admin
from .models import Product, Lesson, LessonAccess


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'owner')


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'video_link', 'duration')


@admin.register(LessonAccess)
class LessonAccessAdmin(admin.ModelAdmin):
    list_display = (
        'user', 'lesson', 'viewed_time', 'viewed', 'last_viewed_date'
    )
    readonly_fields = ('last_viewed_date',)
