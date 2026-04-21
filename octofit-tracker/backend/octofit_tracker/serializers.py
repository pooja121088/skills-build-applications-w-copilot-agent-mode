from rest_framework import serializers
from .models import Team, UserProfile, Activity, Leaderboard, Workout


class TeamSerializer(serializers.ModelSerializer):
    """Serializer for Team model."""
    class Meta:
        model = Team
        fields = ['id', 'name', 'description', 'created_at', 'updated_at']


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializer for UserProfile model."""
    team_name = serializers.CharField(source='team.name', read_only=True)

    class Meta:
        model = UserProfile
        fields = [
            'id', 'user', 'email', 'first_name', 'last_name',
            'team', 'team_name', 'avatar', 'bio', 'created_at', 'updated_at'
        ]


class ActivitySerializer(serializers.ModelSerializer):
    """Serializer for Activity model."""
    user_name = serializers.CharField(
        source='user.first_name', read_only=True
    )

    class Meta:
        model = Activity
        fields = [
            'id', 'user', 'user_name', 'activity_type', 'duration_minutes',
            'calories_burned', 'distance_km', 'description', 'logged_at', 'updated_at'
        ]


class LeaderboardSerializer(serializers.ModelSerializer):
    """Serializer for Leaderboard model."""
    user_name = serializers.CharField(
        source='user.first_name', read_only=True
    )
    team_name = serializers.CharField(
        source='user.team.name', read_only=True
    )

    class Meta:
        model = Leaderboard
        fields = [
            'id', 'user', 'user_name', 'team_name', 'total_activities',
            'total_calories', 'total_distance', 'rank', 'team_rank', 'updated_at'
        ]


class WorkoutSerializer(serializers.ModelSerializer):
    """Serializer for Workout model."""
    class Meta:
        model = Workout
        fields = [
            'id', 'name', 'description', 'difficulty', 'duration_minutes',
            'target_calories', 'exercises', 'created_at', 'updated_at'
        ]
