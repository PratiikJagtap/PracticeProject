from django.db import models

# Create your models means database here.

class students(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    address = models.TextField()
    image = models.ImageField()
    file = models.FileField()


class product(models.Model):
    pass

