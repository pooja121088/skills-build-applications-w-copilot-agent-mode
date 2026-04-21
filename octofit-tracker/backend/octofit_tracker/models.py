from django.db import models
from django.contrib.auth.models import User


class Team(models.Model):
    """Team model for group competitions and activities."""
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'teams'

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    """Extended user profile for fitness tracking."""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, blank=True)
    avatar = models.URLField(blank=True)
    bio = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'users'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Activity(models.Model):
    """Activity model for logging user workouts and fitness activities."""
    ACTIVITY_TYPE_CHOICES = [
        ('running', 'Running'),
        ('cycling', 'Cycling'),
        ('swimming', 'Swimming'),
        ('strength', 'Strength Training'),
        ('yoga', 'Yoga'),
        ('walking', 'Walking'),
        ('other', 'Other'),
    ]

    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='activities')
    activity_type = models.CharField(max_length=50, choices=ACTIVITY_TYPE_CHOICES)
    duration_minutes = models.IntegerField()  # Duration in minutes
    calories_burned = models.IntegerField()
    distance_km = models.FloatField(blank=True, null=True)
    description = models.TextField(blank=True)
    logged_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'activities'

    def __str__(self):
        return f"{self.user} - {self.activity_type}"


class Leaderboard(models.Model):
    """Leaderboard model for tracking user rankings."""
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    total_activities = models.IntegerField(default=0)
    total_calories = models.IntegerField(default=0)
    total_distance = models.FloatField(default=0.0)
    rank = models.IntegerField(default=0)
    team_rank = models.IntegerField(null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'leaderboards'
        ordering = ['rank']

    def __str__(self):
        return f"Leaderboard - {self.user}"


class Workout(models.Model):
    """Workout model for personalized workout suggestions."""
    DIFFICULTY_CHOICES = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    ]

    name = models.CharField(max_length=200)
    description = models.TextField()
    difficulty = models.CharField(max_length=20, choices=DIFFICULTY_CHOICES)
    duration_minutes = models.IntegerField()
    target_calories = models.IntegerField()
    exercises = models.JSONField(default=list)  # List of exercise details
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'workouts'

    def __str__(self):
        return self.name
