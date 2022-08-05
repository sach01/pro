from django.db import models
#import model_utils
#from model_utils import Choices

class Upload(models.Model):#registred polling stations details
    county = models.CharField(max_length=20)
    const = models.CharField(max_length=20)
    ward = models.CharField(max_length=20)
    center = models.CharField(max_length=20, null=True)
    voters = models.IntegerField()
    pstation = models.IntegerField()

    def __str__(self):
        return "{} - {} - {} - {} - {} - {}".format(self.county, self.const, self.ward, self.center, self.voters, self.pstation)

class Seat(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return "{}".format(self.name)

class Aspirant(models.Model):
    name = models.CharField(max_length=20) 
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)

    def __str__(self):
        return "{} - {}".format(self.name, self.seat.name)

class User(models.Model):#user details
    name = models.CharField(max_length=20) 
    role = models.ForeignKey(Aspirant, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} - {} - {}".format(self.name, self.role.seat.name, self.date_created)

class Vote(models.Model):#vote cast
    aspirant = models.ForeignKey(Aspirant, on_delete=models.CASCADE) 
    station = models.ForeignKey(Upload, on_delete=models.CASCADE) 
    vcast = models.PositiveIntegerField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} - {} - {} - {}".format(self.aspirant.name, self.aspirant.seat, self.station.center , self.station, self.vcast, self.date_created)

class Votecast(models.Model):#restricting users view
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vote = models.ForeignKey(Vote, on_delete=models.CASCADE)

    def __str__(self):
        return "{} - {} - {}".format(self.user, self.vote)