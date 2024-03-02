from habitise import models
from habitise import helpers

from django.views import View
from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponse
import json 

class HabitView(View):
    
    def get(self, request):
        habits = models.HabitModel.objects.all()
        habits = helpers.serialize_models(habits)
        return HttpResponse(json.dumps(habits), content_type='application/json')
    
    def post(self, request):
        body = json.loads(request.body)
        
        required_fields = ['name', 'emoji_unicode_hex']
        for field in required_fields:
            if field not in body:
                return HttpResponse(f"Missing required field: {field}", status=400)
        
        habit_name = body.get('name')
        habit_emoji_hex = body.get('emoji_unicode_hex')
        new_habit = models.HabitModel(name=habit_name, emoji_unicode_hex=habit_emoji_hex)
        new_habit.save()
        
        return HttpResponse("Habit created successfully.")