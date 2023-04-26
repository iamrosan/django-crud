from django.db import models

# Create your models here.
class Students(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    addres = models.CharField(max_length=100)
    image = models.ImageField(null=True, blank=True)
    file = models.FileField(null=True,blank=True)

    def __str__(self):
        return self.name


class Car(models.Model):
    car_name = models.CharField(max_length=50)
    speed = models.IntegerField()

    def __str__(self):
        return self.car_name