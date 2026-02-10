from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=255)
    overview = models.TextField()
    release_date = models.DateField()
    rating = models.FloatField()

    def __str__(self):
        return self.title
