from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import ArrayField

from habitise import models as habitise_models
from habitise import helpers

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
        models.IntegerField(null=True),
        default=list
    )
    negative_habits = ArrayField(
        models.IntegerField(null=True),
        default=list
    )
    
    @property
    def habits(self):
        habit_ids = self.positive_habits + self.negative_habits
        habits = habitise_models.HabitModel.objects.filter(id__in=habit_ids)
        return {
            'positive': [helpers.serialize_model(habit) for habit in habits if habit.id in self.positive_habits],
            'negative': [helpers.serialize_model(habit) for habit in habits if habit.id in self.negative_habits]
        }
        
    def add_habit(self, habit_id, habit_type):
        if habit_type == 'positive':
            self.positive_habits.append(habit_id)
        elif habit_type == 'negative':
            self.negative_habits.append(habit_id)
        else:
            raise ValueError(f"Invalid habit type: {habit_type}")
        self.save()