from django.db import models

class Lecture(models.Model):
    subject = models.CharField(max_length=200)
    lecturer = models.CharField(max_length=100)
    place = models.CharField(max_length=200)
    date_time = models.DateTimeField()
    audience = models.IntegerField()

    def __str__(self):
        return self.title
