from django.db import models

class Users(models.Model):
    email = models.EmailField(max_length=254, unique=True)
    firstName = models.CharField(max_length=254)
    lastName = models.CharField(max_length=254)
    address = models.CharField(max_length=254)
    postalCode = models.CharField(max_length=254)
    dateOfBirth = models.DateField()
    healthCardNum = models.CharField(max_length=254)

    class Meta:
        ordering = ['id']
