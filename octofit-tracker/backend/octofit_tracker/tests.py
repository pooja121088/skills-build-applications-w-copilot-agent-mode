from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from .models import Team, UserProfile, Activity, Leaderboard, Workout


class TeamAPITestCase(TestCase):
    """Test cases for Team API."""

    def setUp(self):
        self.client = APIClient()
        self.team = Team.objects.create(
            name='Team Marvel',
            description='Marvel Superheroes'
        )

    def test_create_team(self):
        """Test creating a team."""
        data = {'name': 'Team DC', 'description': 'DC Superheroes'}
        response = self.client.post('/api/teams/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_teams(self):
        """Test listing teams."""
        response = self.client.get('/api/teams/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_retrieve_team(self):
        """Test retrieving a team."""
        response = self.client.get(f'/api/teams/{self.team.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Team Marvel')


class UserProfileAPITestCase(TestCase):
    """Test cases for UserProfile API."""

    def setUp(self):
        self.client = APIClient()
        self.team = Team.objects.create(
            name='Team Marvel',
            description='Marvel Superheroes'
        )
        self.user = User.objects.create_user(
            username='ironman',
            password='password123'
        )
        self.profile = UserProfile.objects.create(
            user=self.user,
            email='ironman@marvel.com',
            first_name='Tony',
            last_name='Stark',
            team=self.team
        )

    def test_create_user_profile(self):
        """Test creating a user profile."""
        new_user = User.objects.create_user(
            username='hulk',
            password='password123'
        )
        data = {
            'user': new_user.id,
            'email': 'hulk@marvel.com',
            'first_name': 'Bruce',
            'last_name': 'Banner',
            'team': self.team.id
        }
        response = self.client.post('/api/users/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_user_profiles(self):
        """Test listing user profiles."""
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_retrieve_user_profile(self):
        """Test retrieving a user profile."""
        response = self.client.get(f'/api/users/{self.profile.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['email'], 'ironman@marvel.com')


class ActivityAPITestCase(TestCase):
    """Test cases for Activity API."""

    def setUp(self):
        self.client = APIClient()
        self.team = Team.objects.create(name='Team Marvel')
        self.user = User.objects.create_user(username='ironman')
        self.profile = UserProfile.objects.create(
            user=self.user,
            email='ironman@marvel.com',
            first_name='Tony',
            last_name='Stark',
            team=self.team
        )
        self.activity = Activity.objects.create(
            user=self.profile,
            activity_type='running',
            duration_minutes=30,
            calories_burned=300,
            distance_km=5.0
        )

    def test_create_activity(self):
        """Test creating an activity."""
        data = {
            'user': self.profile.id,
            'activity_type': 'cycling',
            'duration_minutes': 45,
            'calories_burned': 400,
            'distance_km': 10.0
        }
        response = self.client.post('/api/activities/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_activities(self):
        """Test listing activities."""
        response = self.client.get('/api/activities/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_filter_activities_by_user(self):
        """Test filtering activities by user."""
        response = self.client.get(f'/api/activities/?user_id={self.profile.id}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class LeaderboardAPITestCase(TestCase):
    """Test cases for Leaderboard API."""

    def setUp(self):
        self.client = APIClient()
        self.team = Team.objects.create(name='Team Marvel')
        self.user = User.objects.create_user(username='ironman')
        self.profile = UserProfile.objects.create(
            user=self.user,
            email='ironman@marvel.com',
            first_name='Tony',
            last_name='Stark',
            team=self.team
        )
        self.leaderboard = Leaderboard.objects.create(
            user=self.profile,
            total_activities=5,
            total_calories=1500,
            total_distance=25.0,
            rank=1
        )

    def test_list_leaderboard(self):
        """Test listing leaderboard entries."""
        response = self.client.get('/api/leaderboards/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_leaderboard(self):
        """Test retrieving a leaderboard entry."""
        response = self.client.get(f'/api/leaderboards/{self.leaderboard.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['rank'], 1)


class WorkoutAPITestCase(TestCase):
    """Test cases for Workout API."""

    def setUp(self):
        self.client = APIClient()
        self.workout = Workout.objects.create(
            name='Full Body Strength',
            description='Complete full body workout',
            difficulty='intermediate',
            duration_minutes=60,
            target_calories=500,
            exercises=[]
        )

    def test_create_workout(self):
        """Test creating a workout."""
        data = {
            'name': 'Cardio Blast',
            'description': 'High-intensity cardio',
            'difficulty': 'advanced',
            'duration_minutes': 30,
            'target_calories': 400,
            'exercises': []
        }
        response = self.client.post('/api/workouts/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_workouts(self):
        """Test listing workouts."""
        response = self.client.get('/api/workouts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_workout(self):
        """Test retrieving a workout."""
        response = self.client.get(f'/api/workouts/{self.workout.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Full Body Strength')
