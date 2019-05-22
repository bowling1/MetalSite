from django.db import models
from django.contrib.auth.models import User


class Review(models.Model):
    artist = models.CharField(max_length=100, unique=True)
    album = models.CharField(max_length=100, unique=True)
    content = models.CharField(max_length=150)
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.album) + " - " + str(self.artist)


class Subreview(models.Model):
	# userrating = models.DecimalField(max_digits=3, decimal_places=1)            #Causes and error for some reason
    subject = models.CharField(max_length=150)
    last_updated = models.DateTimeField(auto_now_add=True)
    review = models.ForeignKey(Review, related_name='reviews', on_delete=models.PROTECT)
    starter = models.ForeignKey(User, related_name='reviews', on_delete=models.PROTECT)


class Board(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name


class Topic(models.Model):
    subject = models.CharField(max_length=255)
    last_updated = models.DateTimeField(auto_now_add=True)
    board = models.ForeignKey(Board, related_name='topics', on_delete=models.PROTECT)
    starter = models.ForeignKey(User, related_name='topics', on_delete=models.PROTECT)


class Post(models.Model):
    message = models.TextField(max_length=4000)
    topic = models.ForeignKey(Topic, related_name='posts', on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(User, related_name='posts', on_delete=models.PROTECT)
    updated_by = models.ForeignKey(User, null=True, related_name='+', on_delete=models.PROTECT)