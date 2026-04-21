from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .models import Team, UserProfile, Activity, Leaderboard, Workout
from .serializers import (
    TeamSerializer, UserProfileSerializer, ActivitySerializer,
    LeaderboardSerializer, WorkoutSerializer
)


@api_view(['GET'])
def api_root(request):
    """API root view listing all available endpoints."""
    return Response({
        'users': reverse('userprofile-list', request=request),
        'teams': reverse('team-list', request=request),
        'activities': reverse('activity-list', request=request),
        'leaderboards': reverse('leaderboard-list', request=request),
        'workouts': reverse('workout-list', request=request),
    })


class TeamViewSet(viewsets.ModelViewSet):
    """ViewSet for Team model."""
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class UserProfileViewSet(viewsets.ModelViewSet):
    """ViewSet for UserProfile model."""
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class ActivityViewSet(viewsets.ModelViewSet):
    """ViewSet for Activity model."""
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

    def get_queryset(self):
        """Filter activities by user if user_id is provided."""
        queryset = Activity.objects.all()
        user_id = self.request.query_params.get('user_id')
        if user_id:
            queryset = queryset.filter(user_id=user_id)
        return queryset


class LeaderboardViewSet(viewsets.ModelViewSet):
    """ViewSet for Leaderboard model."""
    queryset = Leaderboard.objects.all()
    serializer_class = LeaderboardSerializer


class WorkoutViewSet(viewsets.ModelViewSet):
    """ViewSet for Workout model."""
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer
