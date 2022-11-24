from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    phone = models.CharField(max_length=200,null=True,blank=True)
    address = models.CharField(max_length=200,null=True,blank=True)
    position = models.CharField(max_length=200,null=True,blank=True)
    image = models.ImageField(upload_to='users',null=True,blank=True)

class Zone(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class CityTown(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='cit-&town/')

    def __str__(self):
        return self.name

class Region(models.Model):
    zone = models.ForeignKey(Zone, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='regions/')

    def __str__(self):
        return self.name

class Convensere(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class WeeklyOffers(models.Model):
    image = models.ImageField(upload_to='weeklyOffers/')
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    content = models.TextField()
    peoples = models.IntegerField()
    phone = models.CharField(max_length=200)
    email = models.EmailField()
    address = models.CharField(max_length=200)
    t_map = models.TextField()
    convensere = models.ForeignKey(Convensere, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

class Country(models.Model):
    name = models.CharField(max_length=200)
    population = models.CharField(max_length=200)
    territory = models.CharField(max_length=200)
    avg_price = models.CharField(max_length=200)
    content = models.TextField()
    city_town = models.ForeignKey(CityTown,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='Country')
    region = models.ForeignKey(Region,on_delete=models.CASCADE)
    weekly_offres = models.ForeignKey(WeeklyOffers,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    numbers = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    wekkly_offres = models.ForeignKey(WeeklyOffers,on_delete=models.CASCADE)


    def __str__(self):
        return self.user.name + " " + str(self.wekkly_offres.name)
