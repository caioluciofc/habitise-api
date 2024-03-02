from django.views import View
from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponse
import json 
from datetime import datetime

from habitise import models

class UserHabitView(View):
    
    def get(self, request, user_id):
        user = get_object_or_404(models.User, id=user_id)
        return HttpResponse(json.dumps(user.habits), content_type='application/json')
    
    def post(self, request, user_id):
        body = json.loads(request.body)
        
        required_fields = ['habit_id', 'habit_type']
        for field in required_fields:
            if field not in body:
                return HttpResponse(f"Missing required field: {field}", status=400)
            
        habit = body.get('habit_id')
        habit_type = body.get('habit_type')
        
        user = get_object_or_404(models.User, id=user_id)
        user.add_habit(habit, habit_type)
        return HttpResponse("Habit added successfully.")