from django.db import models

# Create your models here.

class Game(models.Model):
    game_date = models.DateTimeField("Game day")
    duration = models.CharField(max_length=10, default="3h")
    system = models.CharField(max_length=20)
    players = models.CharField(max_length=200)
    title = models.CharField(max_length=200, default="WIP")
    description = models.CharField(max_length=500)
    def __str__(self):
        return self.title
