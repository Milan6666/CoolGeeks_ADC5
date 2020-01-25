from django.db import models

# model to register the new user
class Registration(models.Model):

    class Gender(models.TextChoices): #enummeration for choices
        Male='male'
        Female='female'
        Hidden='notToSay'

    first_name=models.CharField('first name',max_length=100)
    last_name=models.CharField('last name',max_length=100)
    gender=models.CharField('gender',max_length=20,choices=Gender.choices)
    phone_number=models.CharField('phone number',max_length=13,unique=True)
    email=models.CharField('Mail address',max_length=45,unique=True)
    date_of_birth=models.DateField('birth date')
    address=models.TextField('Address')
    password=models.CharField('password',max_length=200)

