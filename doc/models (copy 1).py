from django.db import models

# Create your models here.

#from django.db.models import Count
#sys.setrecursionlimit(2000)

class County(models.Model):
    name = models.CharField(max_length=20) #county name
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} - {}".format(self.name, self.date_created)

class SubCounty(models.Model):
    name = models.CharField(max_length=20) #sub_county name
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} - {}".format(self.name, self.date_created)

class Ward(models.Model):
    sub_county = models.ForeignKey(SubCounty, on_delete=models.CASCADE) #under which ward
    name = models.CharField(max_length=20) #ward name
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} - {} - {}".format(self.name, self.sub_county, self.date_created)

class Location(models.Model):
    ward = models.ForeignKey(Ward, on_delete=models.CASCADE) #under which ward
    #name = models.CharField(max_length=20) #ward name
    pstation = models.CharField(max_length=20) #polling station
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} - {} - {}".format(self.name, self.pstation, self.ward, self.date_created)

class Leaders(models.Model):
    name = models.CharField(max_length=20) 
    seat = models.CharField(max_length=20)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} - {} - {}".format( self.name, self.seat, self.date_created)

class Election(models.Model):
    leaders = models.ForeignKey(Leaders, on_delete=models.CASCADE) 
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    incoming_votes = models.PositiveIntegerField() 
    date_created = models.DateTimeField(auto_now_add=True)
    "voter=actual voters number (max number of voters)"
    "incoming_votes= "
    "sum it up per location"

    def __str__(self):
        return "{} - {} - {}".format(self.leader, self.location, self.incoming_votes, self.date_created)