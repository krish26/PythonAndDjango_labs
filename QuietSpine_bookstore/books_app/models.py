from django.db import models

class booknames(models.Model):
    title=models.CharField(max_length=30)
    author=models.CharField(max_length=30)
    content=models.CharField(max_length=300)





