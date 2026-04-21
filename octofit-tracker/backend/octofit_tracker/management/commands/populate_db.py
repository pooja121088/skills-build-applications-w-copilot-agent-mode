from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from octofit_tracker.models import Team, UserProfile, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()
        UserProfile.objects.all().delete()
        Team.objects.all().delete()
        User.objects.all().delete()

        # Create Teams
        marvel = Team.objects.create(name='Team Marvel', description='Marvel Superheroes')
        dc = Team.objects.create(name='Team DC', description='DC Superheroes')

        # Create Users and Profiles
        tony = User.objects.create_user(username='ironman', password='password123')
        bruce = User.objects.create_user(username='hulk', password='password123')
        clark = User.objects.create_user(username='superman', password='password123')
        diana = User.objects.create_user(username='wonderwoman', password='password123')

        tony_profile = UserProfile.objects.create(user=tony, email='ironman@marvel.com', first_name='Tony', last_name='Stark', team=marvel)
        bruce_profile = UserProfile.objects.create(user=bruce, email='hulk@marvel.com', first_name='Bruce', last_name='Banner', team=marvel)
        clark_profile = UserProfile.objects.create(user=clark, email='superman@dc.com', first_name='Clark', last_name='Kent', team=dc)
        diana_profile = UserProfile.objects.create(user=diana, email='wonderwoman@dc.com', first_name='Diana', last_name='Prince', team=dc)

        # Create Activities
        Activity.objects.create(user=tony_profile, activity_type='running', duration_minutes=30, calories_burned=300, distance_km=5.0)
        Activity.objects.create(user=bruce_profile, activity_type='cycling', duration_minutes=45, calories_burned=400, distance_km=15.0)
        Activity.objects.create(user=clark_profile, activity_type='swimming', duration_minutes=60, calories_burned=500, distance_km=2.0)
        Activity.objects.create(user=diana_profile, activity_type='yoga', duration_minutes=40, calories_burned=200)

        # Create Leaderboards
        Leaderboard.objects.create(user=tony_profile, total_activities=1, total_calories=300, total_distance=5.0, rank=1, team_rank=1)
        Leaderboard.objects.create(user=bruce_profile, total_activities=1, total_calories=400, total_distance=15.0, rank=2, team_rank=2)
        Leaderboard.objects.create(user=clark_profile, total_activities=1, total_calories=500, total_distance=2.0, rank=1, team_rank=1)
        Leaderboard.objects.create(user=diana_profile, total_activities=1, total_calories=200, total_distance=0.0, rank=2, team_rank=2)

        # Create Workouts
        Workout.objects.create(
            name='Full Body Strength',
            description='Complete full body workout',
            difficulty='intermediate',
            duration_minutes=60,
            target_calories=500,
            exercises=[{'name': 'Push Ups', 'reps': 20}, {'name': 'Squats', 'reps': 30}]
        )
        Workout.objects.create(
            name='Cardio Blast',
            description='High-intensity cardio',
            difficulty='advanced',
            duration_minutes=30,
            target_calories=400,
            exercises=[{'name': 'Jump Rope', 'minutes': 10}, {'name': 'Sprints', 'minutes': 20}]
        )

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
