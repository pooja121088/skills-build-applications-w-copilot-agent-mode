from django.contrib import admin
from .models import Team, UserProfile, Activity, Leaderboard, Workout


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at', 'updated_at']
    search_fields = ['name']


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'team', 'created_at']
    search_fields = ['email', 'first_name', 'last_name']
    list_filter = ['team', 'created_at']


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ['user', 'activity_type', 'duration_minutes', 'calories_burned', 'logged_at']
    search_fields = ['user__first_name', 'user__last_name']
    list_filter = ['activity_type', 'logged_at']


@admin.register(Leaderboard)
class LeaderboardAdmin(admin.ModelAdmin):
    list_display = ['user', 'rank', 'total_activities', 'total_calories', 'team_rank']
    search_fields = ['user__first_name', 'user__last_name']
    list_filter = ['rank', 'updated_at']


@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ['name', 'difficulty', 'duration_minutes', 'target_calories', 'created_at']
    search_fields = ['name']
    list_filter = ['difficulty', 'created_at']
