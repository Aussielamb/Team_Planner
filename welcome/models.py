from django.db import models


class TeamName(models.Model):
    team = models.CharField(max_length=50)

    def __str__(self):
        return self.team


class Location(models.Model):
    location = models.CharField(max_length=100)
    state = models.CharField(max_length=30)
    suburb = models.CharField(max_length=30)
    physical_Address = models.CharField(max_length=100)
    phone_Number = models.CharField(max_length=30)

    def __str__(self):
        return self.location


class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100, choices=(('Manager', 'Manager'), ('Member', 'Member')))
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    team = models.ForeignKey(TeamName, on_delete=models.CASCADE)
    start_date = models.DateField()

    def __str__(self):
        return self.name


class CustomUser(models.Model):
    # Your model fields here

    class Meta:
        permissions = [
            ("can_edit_forms", "Can edit forms"),
        ]
