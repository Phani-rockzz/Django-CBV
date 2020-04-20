from django.db import models

# Create your models here.
class school(models.Model):
    name = models.CharField(max_length=128)
    principal = models.CharField(max_length=128)
    location = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class student(models.Model):
    name = models.CharField(max_length=128)
    age = models.PositiveIntegerField()
    school = models.ForeignKey(school,related_name='students',on_delete=models.CASCADE)

    def __str__(self):
        return self.name
