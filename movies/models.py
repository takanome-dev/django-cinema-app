from django.db import models

class Genre(models.Model):
  name = models.CharField(max_length=255)

  def __str__(self):
    return self.name

class Movie(models.Model):
  title = models.CharField(max_length=255)
  overview = models.CharField(max_length=500)
  release_date = models.CharField(max_length=10)
  genre = models.ForeignKey(Genre,on_delete=models.CASCADE)
  url = models.CharField(max_length=255)
  vote_average = models.IntegerField()
  vote_count = models.IntegerField()