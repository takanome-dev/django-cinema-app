from django.db import models

class Genre(models.Model):
  name = models.CharField(max_length=255)

class Movie(models.Model):
  title = models.CharField(max_length=255)
  description = models.CharField(max_length=500)
  release_year = models.IntegerField()
  genre = models.ForeignKey(Genre,on_delete=models.CASCADE)