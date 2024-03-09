from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone

User = get_user_model()


class Product(models.Model):
    owner = models.ForeignKey(User, on_delete=models.PROTECT)


class Lesson(models.Model):

    title = models.CharField(max_length=200)
    video_link = models.URLField()
    duration = models.IntegerField()
    products = models.ManyToManyField(Product)

    def __str__(self):
        return f'{self.pk}: {self.title}'


class LessonAccess(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    viewed_time = models.IntegerField(default=0)
    viewed = models.BooleanField(default=False)
    last_viewed_date = models.DateTimeField(null=True)

    def save(self, *args, **kwargs):
        # если объект еще не создан
        if self.pk:
            self.last_viewed_date = timezone.now()

        if self.viewed_time >= self.lesson.duration * 0.8:
            self.viewed = True

        super().save(*args, **kwargs)
