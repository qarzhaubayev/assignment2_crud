from django.db import models
from django.urls import reverse


# Create your models here.

class DiseaseType(models.Model):
    diseaseID = models.IntegerField(primary_key=True)
    diseaseDescription = models.CharField(max_length=140)

class Country(models.Model):
    cname = models.CharField(max_length=50, primary_key=True)
    population = models.BigIntegerField()

class Disease(models.Model):
    disease_code = models.CharField(max_length=50, primary_key=True)
    pathogen = models.CharField(max_length=20)
    description = models.CharField(max_length=140)
    diseaseID = models.ForeignKey(DiseaseType, on_delete=models.CASCADE)

class Discover(models.Model):
    cname = models.ForeignKey(Country, on_delete=models.CASCADE)
    disease_code = models.ForeignKey(Disease, on_delete=models.CASCADE)
    first_enc_date = models.DateField()
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['cname', 'disease_code'], name='Discover_constraint'
            )
        ]
    

class Users(models.Model):
    email = models.CharField(max_length=60, primary_key= True)
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=40)
    salary = models.IntegerField()
    phone = models.CharField(max_length=20)
    cname = models.ForeignKey(Country, on_delete= models.CASCADE)


class PublicServant(models.Model):
    email = models.OneToOneField(Users, on_delete= models.CASCADE, primary_key= True)
    department = models.CharField(max_length=50)


class Doctor(models.Model):
    email = models.OneToOneField(Users, on_delete= models.CASCADE, primary_key=True)
    degree = models.CharField(max_length=20)

class Specialize(models.Model):
    diseaseID = models.ForeignKey(DiseaseType, on_delete= models.CASCADE)
    email = models.OneToOneField(Doctor, on_delete=models.CASCADE)
    class Meta: 
        constraints = [
            models.UniqueConstraint(
                fields= ['diseaseID', 'email'], name='specialize_constraint'
            )
        ]

class Record(models.Model):
    cname = models.ForeignKey(Country, on_delete= models.CASCADE)
    email = models.ForeignKey(PublicServant,  on_delete= models.CASCADE)
    disease_code = models.ForeignKey(Disease, on_delete= models.CASCADE)
    total_deaths = models.IntegerField()
    total_patients = models.IntegerField()
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields= ['email','cname','disease_code'], name='record_constraint'
            )
        ]