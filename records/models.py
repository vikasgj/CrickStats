from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Player(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Match(models.Model):
    FORMAT_CHOICES = [
        ('ODI', 'One Day International'),
        ('T20', 'Twenty20'),
        ('TEST', 'Test Match'),
    ]
    date = models.DateField()
    format = models.CharField(max_length=10, choices=FORMAT_CHOICES)
    team1 = models.ForeignKey(Team, related_name='team1', on_delete=models.CASCADE)
    team2 = models.ForeignKey(Team, related_name='team2', on_delete=models.CASCADE)

class Record(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    runs = models.PositiveIntegerField()
    wickets = models.PositiveIntegerField(default=0)
    is_not_out = models.BooleanField(default=False)
