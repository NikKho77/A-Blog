from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()

    def __str__(self):
        return self.title + '|' + str(self.author)

class History(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()

class Contacts(models.Model):
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    adress = models.CharField(max_length=120)

class Prices(models.Model):
    price1 = models.CharField(max_length=150 , blank=True)
    price2 = models.CharField(max_length=150 , blank=True)
    price3 = models.CharField(max_length=150 , blank=True)
    price4 = models.CharField(max_length=150 , blank=True)
    price5 = models.CharField(max_length=150 , blank=True)
    price6 = models.CharField(max_length=150, blank=True)
    price7 = models.CharField(max_length=150, blank=True)
    price8 = models.CharField(max_length=150, blank=True)
    price9 = models.CharField(max_length=150, blank=True)
    price10 = models.CharField(max_length=150, blank=True)
    price11 = models.CharField(max_length=150, blank=True)
    price12 = models.CharField(max_length=150, blank=True)
    price13 = models.CharField(max_length=150, blank=True)
    price14 = models.CharField(max_length=150, blank=True)
    price15 = models.CharField(max_length=150, blank=True)
    price16 = models.CharField(max_length=150, blank=True)
    price17 = models.CharField(max_length=150, blank=True)
    price18 = models.CharField(max_length=150, blank=True)
    price19 = models.CharField(max_length=150, blank=True)
    price20 = models.CharField(max_length=150, blank=True)
    price21 = models.CharField(max_length=150, blank=True)


class Hours(models.Model):
    monday = models.CharField(max_length=150)
    tuesday = models.CharField(max_length=150)
    wednesday = models.CharField(max_length=150)
    thursday = models.CharField(max_length=150)
    friday = models.CharField(max_length=150)
    saturday = models.CharField(max_length=150)
    sunday = models.CharField(max_length=150)
