from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _

# Create your models here.

class Subscribe(models.Model):
    # information
    email = models.EmailField('Email', max_length = 50)

    # moderations
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email