from django.db import models

class TrackedHabit(models.Model):
    '''This class creates an abstract model that contains the tracked habits
    by the user with the date that the habit was tracked.
    '''
    
    habit = models.ForeignKey('HabitModel', on_delete=models.PROTECT)
    done_at = models.DateTimeField()
    user = models.ForeignKey('UserModel', on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)