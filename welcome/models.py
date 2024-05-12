from django.db import models


# db model for team name
class TeamName(models.Model):
    team = models.CharField(max_length=50)

    def __str__(self):
        return self.team


# db model for locations w/ relevant data
class Location(models.Model):
    location = models.CharField(max_length=100)
    state = models.CharField(max_length=30)
    suburb = models.CharField(max_length=30)
    physical_Address = models.CharField(max_length=100)
    phone_Number = models.CharField(max_length=30)

    def __str__(self):
        return self.location


# db model for team members and managers collectively
class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100, choices=(('Manager', 'Manager'), ('Member', 'Member')))
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    team = models.ForeignKey(TeamName, on_delete=models.CASCADE)
    start_date = models.DateField()

    def __str__(self):
        return self.name