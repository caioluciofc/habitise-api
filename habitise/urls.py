from django.contrib import admin
from django.urls import path
from habitise import views

urlpatterns = [
    path('', views.hello_world, name='hello_world'),
    path('admin/', admin.site.urls),
    path('track-habit/', views.TrackHabitView.as_view(), name='track_habit'),
    path('habits/', views.HabitView.as_view(), name='habits'),
    path('user-habits/<int:user_id>/', views.UserHabitView.as_view(), name='user_habits'),
]
