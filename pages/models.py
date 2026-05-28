from django.db import models

class products(models.Model):
    name=models.CharField(max_length=50)
    price=models.IntegerField(max_length=50)
    image=models.ImageField(upload_to='products/')
    desc=models.TextField()
