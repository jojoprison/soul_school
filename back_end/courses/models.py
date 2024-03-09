from django.contrib.auth.models import User
from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Enrollment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrolled_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} enrolled in {self.course.title}"


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
