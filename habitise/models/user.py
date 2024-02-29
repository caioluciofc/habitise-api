from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import ArrayField

class User(AbstractUser):
    '''This abstract class contains user data alongside the positives
    and negatives habits that the user wants to track.
    '''
    
    email = models.EmailField(blank=False, db_index=True)
    username = models.CharField(max_length=25, unique=True)
    full_name = models.CharField(max_length=100, blank=True)
    last_seen = models.DateTimeField(auto_now=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    positive_habits = ArrayField(
        models.CharField(max_length=10, null=True),
        default=list
    )
    negative_habits = ArrayField(
        models.CharField(max_length=10, null=True),
        default=list
    )
    