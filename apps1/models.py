from django.db import models

# Create your models here.
class travel(models.Model):
    name = models.CharField(max_length = 100)
    img = models.ImageField(upload_to = 'pics')
    desp = models.TextField()
    price = models.IntegerField()
