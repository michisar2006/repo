from django.db import models

class ChampionshipTemplate(models.Model):
    """Represents an abstract football championship."""
    name = models.CharField(max_length=50)
    size = models.IntegerField(default=2)

    def __str__(self):
        return self.name

class Phase(models.Model):
    name = models.CharField(max_length=50)
    championship = models.ForeignKey(
        ChampionshipTemplate, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(default="", max_length=100)
    image = models.ImageField(
        upload_to='teams/')
    

class Championship(models.Model):
    starts = models.DateTimeField(auto_now=False, auto_now_add=False)
    ends = models.DateTimeField(auto_now=False, auto_now_add=False)

    championshipTemplate = models.ForeignKey(
        ChampionshipTemplate, on_delete=models.CASCADE, null=True, blank=True)
    
class RegisteredTeam(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    championship = models.ForeignKey(Championship, on_delete=models.CASCADE)

class Match(models.Model):
    NOT_STARTED = "not started"
    PLAYING = "playing"
    ENDED = "ended"

    player1 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='player1_matches')
    player2 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='player2_matches')

    player1_goals = models.IntegerField(default=0, null=True, blank=True)
    player2_goals = models.IntegerField(default=0, null=True, blank=True)

    status = models.BooleanField(default=NOT_STARTED)
    
    def __str__(self):
        return "{} vs {}".format(self.player1, self.player2)

