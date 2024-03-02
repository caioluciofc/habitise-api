from django.views import View
from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponse
import json 
from datetime import datetime

from habitise import models
    
def hello_world(request):
    return HttpResponse('Hello, World!')

class TrackHabitView(View):
    """View to track a habit"""
    
    def post(self, request):
        body = json.loads(request.body)
        
        required_fields = ['habit_id', 'user_id', 'done_at']
        for field in required_fields:
            if field not in body:
                return HttpResponse(f"Missing required field: {field}", status=400)
        
        habit_id = body.get('habit_id')
        user_id = body.get('user_id')
        done_at = datetime.fromtimestamp(body.get('done_at'))

        new_track = models.TrackedHabit(
            habit_id=habit_id,
            user_id=user_id,
            done_at=datetime.fromtimestamp(done_at)
        )
        new_track.save()
        
        return HttpResponse("Habit tracked successfully.")

    def delete(self, request):
        body = json.loads(request.body)
        
        required_fields = ['tracked_habit_id']
        for field in required_fields:
            if field not in body:
                return HttpResponse(f"Missing required field: {field}", status=400)
        
        tracked_habit_id = body.get('tracked_habit_id')
        tracked_habit = models.TrackedHabit.objects.get(id=tracked_habit_id)
        tracked_habit.delete()
        
        return HttpResponse("Habit untracked successfully.")