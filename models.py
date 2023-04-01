from django.db import models

# Create your models here.
class customer(models.Model):
    firstname = models.CharField(max_length=200,null=True)
    lastname = models.CharField(max_length=200,null=True)
    email = models.CharField(max_length=200,null=True)
    username = models.CharField(max_length=200, null=True)
    password = models.CharField(max_length=200, null=True)


class crud(models.Model):
    name = models.CharField(max_length=200,null=True)
    age = models.CharField(max_length=200,null=True)
    email = models.CharField(max_length=200,null=True)
    address = models.CharField(max_length=200,null=True)
    image = models.ImageField(null=True,blank=True,upload_to ="images/")