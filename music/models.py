from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=100)
    songs = models.ManyToManyField('Song')

    def __str__(self):
        return self.name

class Song(models.Model):

    name = models.CharField(
        blank=True,
        null=True,
        max_length=50
    )
    img = models.ImageField(
        upload_to='musics/',
        blank=True,
        null=True
    )
    description = models.TextField(
        blank=True,
        null=True,
        max_length=360
    )
    file = models.FileField(
        upload_to='music/'
    )
    link = models.URLField(max_length=500)

    def __str__(self):
        return f'{self.name}'

