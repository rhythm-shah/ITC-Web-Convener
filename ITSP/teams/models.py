from django.db import models


class Team(models.Model):
    teamName = models.CharField(max_length=50)
    teamID = models.CharField(max_length=20)
    nameTeamMembers = models.CharField(max_length=50)

    def __str__(self):
        return self.teamName


class NameTeamMembers(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    nameTeamMembers = models.CharField(max_length=50)

    def __str__(self):
        return self.nameTeamMembers
