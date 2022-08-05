from django.db import models
#import model_utils
#from model_utils import Choices

class Upload(models.Model):
    county = models.CharField(max_length=20)
    const = models.CharField(max_length=20)
    ward = models.CharField(max_length=20)
    center = models.CharField(max_length=20, null=True)
    voters = models.IntegerField()
    pstation = models.IntegerField()

    def __str__(self):
        return "{} - {} - {} - {} - {} - {}".format(self.county, self.const, self.ward, self.center, self.voters, self.pstation)

class County(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return "{}".format(self.name)

class Station(models.Model):
    county = models.ForeignKey(County, on_delete=models.CASCADE)
    const = models.CharField(max_length=20) 
    ward = models.CharField(max_length=20) #ward
    location = models.CharField(max_length=20)
    #voters = models.CharField(max_length=20)
    #pstation = models.CharField(max_length=20) #polling station

    def __str__(self):
        return "{} - {} - {} - {}".format(self.county, self.const, self.ward, self.location)

class Aspirant(models.Model):
    state = (
    ('Governor', 'governor'),
    ('Dgovernor', 'dgovernor'),
    ('Senate', 'senate'),
    ('Mp', 'mp'),
    ('Mca', 'mca'),
    ('Wrep', 'wrep'),
    )
    name = models.CharField(max_length=20) 
    #seat = models.CharField(choices=state)
    seat =  models.CharField(max_length = 20, choices = state, default = 'Governor')

    def __str__(self):
        return "{} - {}".format(self.name, self.seat)

class Vote(models.Model):
    aspirant = models.ForeignKey(Aspirant, on_delete=models.CASCADE) 
    station = models.ForeignKey(Station, on_delete=models.CASCADE) 
    vcast = models.PositiveIntegerField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} - {} - {} - {}".format(self.aspirant, self.station, self.vcast, self.date_created)