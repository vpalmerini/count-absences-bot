from django.db import models

class User(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    username = models.CharField(max_length=50)

    def __str__(self):
        return self.username


class Chat(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    state = models.CharField(max_length=5, default='s0')

    def __str__(self):
        return str(self.id)


class Course(models.Model):
    initials = models.CharField(max_length=8, primary_key=True)
    workload = models.IntegerField(default=4)
    user = models.ManyToManyField('User', related_name='courses')
    day = models.ManyToManyField('Day')

    def __str__(self):
        return self.initials

class Day(models.Model):
    seg = 'seg'
    ter = 'ter'
    qua = 'qua'
    qui = 'qui'
    sex = 'sex'
    sab = 'sab'
    dom = 'dom'

    DAYS_CHOICES = (
        (seg,'segunda'),
        (ter,'terça'),
        (qua,'quarta'),
        (qui,'quinta'),
        (sex,'sexta'),
        (sab,'sábado'),
        (dom,'domingo')
    )

    day = models.CharField(max_length=7, choices=DAYS_CHOICES, primary_key=True, default=seg)

    def __str__(self):
        return self.day


class Time(models.Model):
    time = models.TimeField(default='8:00')
    day = models.ManyToManyField('Day')

    def __str__(self):
        return str(self.time)
