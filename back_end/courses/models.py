
from django.contrib.auth.models import User
from django.db import models


class Product(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)


class Lesson(models.Model):
    title = models.CharField(max_length=200)
    video_link = models.URLField()
    duration = models.IntegerField()
    products = models.ManyToManyField(Product)


class LessonAccess(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    viewed_time = models.IntegerField()
    viewed = models.BooleanField(default=False)