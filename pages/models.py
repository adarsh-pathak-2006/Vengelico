from django.db import models

class products(models.Model):
    name=models.CharField(max_length=50)
    price=models.IntegerField()
    image=models.ImageField(upload_to='products/')
    desc=models.TextField()


class contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    message=models.TextField()
