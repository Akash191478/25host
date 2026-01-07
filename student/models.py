from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField()
    email = models.EmailField()
    age = models.IntegerField()
    image = models.ImageField()
    def __str__(self):
        return self.name