from django.db import models

class ticket(models.Model):
   full_name= models.CharField(max_length=20,unique=False)
   email=models.CharField(max_length=50,unique=False)
   textarea=models.TextField(max_length=500,unique=False)
   Category=models.CharField(max_length=50,unique=False)

