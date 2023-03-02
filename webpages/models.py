from django.db import models

# Create your models here.

class contact(models.Model):
    email=models.CharField(max_length=22)
    name=models.CharField(max_length=22)
    subject=models.CharField(max_length=122)
    message=models.CharField(max_length=500)
    date=models.DateField()
    def __str__(self):
        return self.name