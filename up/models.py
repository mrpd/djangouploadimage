from django.db import models

# Create your models here.
class fileUp(models.Model):
    fileupp=models.ImageField(upload_to='doc/%Y/%m/%d')

    
class something(models.Model):
    name=models.CharField(max_length=300)
