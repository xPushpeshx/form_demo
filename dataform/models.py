from django.db import models

class regFORM(models.Model):
    name=models.CharField(max_length=50)
    phoneno=models.IntegerField()
    dob=models.DateField()
    email=models.EmailField()