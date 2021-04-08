from django.db import models
from django.utils import timezone
from django.core import validators
from django.contrib.auth.models import AbstractUser
import datetime


class Period(models.Model):
    name = models.CharField(max_length=20)
    duration_from_start = models.DurationField('duration from start')
    step = models.DurationField('step')
    isDailyData = models.BooleanField()
    sort = models.IntegerField()

    def __str__(self) -> str:
        return self.name

class Place(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name


class Environment(models.Model):
    postdate = models.DateTimeField('post date', default=timezone.now)
    place = models.ForeignKey(Place, default='unknown',
                              on_delete=models.SET_DEFAULT)
    temperature = models.FloatField('temperature', validators=[
        validators.MinValueValidator(-99.999),
        validators.MaxValueValidator(99.999)
    ])
    pressure = models.FloatField('pressure', validators=[
        validators.MinValueValidator(0),
        validators.MaxValueValidator(9999.999)
    ])
    humidity = models.FloatField('humidity', validators=[
        validators.MinValueValidator(0),
        validators.MaxValueValidator(99.999)
    ])
    lux = models.FloatField('lux', validators=[
        validators.MinValueValidator(0),
        validators.MaxValueValidator(9999.999)
    ])

    def __str__(self) -> str:
        jst = datetime.timezone(datetime.timedelta(hours=+9), 'Asia/Tokyo')
        return f'{self.postdate.astimezone(jst)}, {self.place}'


class CustomUser(AbstractUser):
    pass

class Photo(models.Model):
    title = models.CharField(max_length=32)
    image = models.ImageField(upload_to='photo/',blank=True, null=True)
    postdate = models.DateTimeField(auto_now_add=True)
    place = models.ForeignKey(Place, default='unknown',
                              on_delete=models.SET_DEFAULT)

    def publish(self):
        self.post_date = timezone.now()
        self.save()
