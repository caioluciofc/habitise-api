from django.db import models

class HabitModel(models.Model):
    '''This class contains the habits that are able to be tracked on 
    the application, it contains habits that all users might create to
    support an auto-complete feature that will avoid duplication of data
    on the database.
    '''
    
    name = models.CharField(max_lenght=15, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)