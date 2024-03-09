from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import LessonViewSet, ProductStatisticsViewSet, ProductLessonsViewSet

router = DefaultRouter()

router.register(r'lessons', LessonViewSet, basename='lesson')
router.register(
    r'products/(?P<product_id>\d+)/lessons',
    ProductLessonsViewSet,
    basename='product-lessons'
)
router.register(
    r'products-statistics',
    ProductStatisticsViewSet,
    basename='products-statistics'
)

urlpatterns = [
    path('', include(router.urls)),
]
