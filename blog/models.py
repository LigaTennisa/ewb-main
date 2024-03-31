from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import datetime


class Post(models.Model):
    COURT_CHOICES = (
        ('Court A', 'Court A'),
        ('Court B', 'Court B'),
        ('Court C', 'Court C'),
    )

    title = models.CharField('Заголовок', max_length=120)

    court = models.CharField('Корт', max_length=20,
                             choices=COURT_CHOICES, default='Court A')

    training_date = models.DateField(
        'Дата', default=datetime.date.today)
    training_time = models.TimeField(
        'Время', default=datetime.time(0, 0))
    preferences = models.CharField('Пожелания', max_length=20, default='')

    published_at = models.DateTimeField('Опубликовано', default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def str(self):
        return self.title

    class Meta:
        ordering = ['-published_at']
