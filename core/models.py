from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _

# Create your models here.


MODEL_CHOICES= [
    ('1', 'Select the role *'),
    ('2', 'Volunteer'),
    ('3', 'Partner'),
    ('4', 'Mentor'),
    ('5', 'Donor')
    ]


class Subscribe(models.Model):
    # information
    email = models.EmailField('Email', max_length = 50, unique=True)

    # moderations
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email



class Involved(models.Model):
    
    # information
    name = models.CharField('Ad', max_length = 256)
    email = models.EmailField('Email', max_length = 50)
    number = models.CharField('Telefon nömrəsi', max_length = 20)
    membership_type = models.CharField('Membership type', choices = MODEL_CHOICES, default = 'Select the role *', max_length = 256)
    message = models.TextField('Mesaj', max_length = 5000)

    # moderations
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class Statitics(models.Model):
    projects = models.IntegerField('local and international', default = 0)
    eur = models.IntegerField('funds raised', default = 0)
    females = models.IntegerField('AWiS volunteers', default = 0)
    girls_mentees = models.IntegerField('AWiS mentees', default = 0)
    girls_regional = models.IntegerField('regional ambassadors', default = 0)
    followers = models.IntegerField('social media followers', default = 0)
    women = models.IntegerField('experts in network', default = 0)