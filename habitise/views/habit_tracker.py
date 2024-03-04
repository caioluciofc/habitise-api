from django.views import View
from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponse
import json 
from datetime import datetime, date, timedelta

from habitise import models
from habitise import helpers
    
def hello_world(request):
    return HttpResponse('Hello, World!')

class TrackHabitView(View):
    """View to track a habit"""
    
    def get(self, request):
        month = int(request.GET.get('month'))
        user_id = request.GET.get('user_id')
        initial_date = date(year=datetime.now().year, month=month, day=1)
        final_date = initial_date.replace(month=month+1) - timedelta(days=1)
        tracked_habits = models.TrackedHabitsModel.objects.filter(user_id=user_id, done_at__range=[initial_date, final_date])
        tracked_habits_json = helpers.serialize_models(tracked_habits)
        return HttpResponse(json.dumps(tracked_habits_json), content_type='application/json')
    
    def post(self, request):
        body = json.loads(request.body)
        
        required_fields = ['habit_id', 'done_at', 'user_id']
        for field in required_fields:
            if field not in body:
                return HttpResponse(f"Missing required field: {field}", status=400)
        
        habit_id = body.get('habit_id')
        user_id = body.get('user_id')
        done_at = datetime.fromtimestamp(body.get('done_at'))

        new_track = models.TrackedHabitsModel(
            habit_id=habit_id,
            user_id=user_id,
            done_at=done_at
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
        tracked_habit = models.TrackedHabitsModel.objects.get(id=tracked_habit_id)
        tracked_habit.delete()
        
        return HttpResponse("Habit untracked successfully.")