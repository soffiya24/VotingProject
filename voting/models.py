from django.db import models

# Create your models here.
class ContactUS(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    message=models.TextField(default='Nothing')


class Election(models.Model):
    name = models.CharField(max_length=100)
    content = models.CharField(max_length=100)
    is_over = models.BooleanField(default=False)

class Candidate_votes(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=100)    
    Election = models.ForeignKey(to=Election, on_delete=models.CASCADE)
    votes = models.IntegerField(default=0)   

class Voted(models.Model):
    user = models.CharField(max_length=100)
    vote = models.BooleanField() 
   