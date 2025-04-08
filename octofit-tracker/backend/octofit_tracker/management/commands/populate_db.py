from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create test users
        user1 = User.objects.create(email='john.doe@example.com', name='John Doe')
        user2 = User.objects.create(email='jane.smith@example.com', name='Jane Smith')

        # Create test teams
        team1 = Team.objects.create(name='Team Alpha')
        team2 = Team.objects.create(name='Team Beta')

        # Add users to teams
        team1.members.add(user1)
        team2.members.add(user2)

        # Create test activities
        Activity.objects.create(user=user1, description='Running 5km')
        Activity.objects.create(user=user2, description='Cycling 10km')

        # Create test leaderboard entries
        Leaderboard.objects.create(team=team1, score=100)
        Leaderboard.objects.create(team=team2, score=80)

        # Create test workouts
        Workout.objects.create(user=user1, type='Cardio', duration=30)
        Workout.objects.create(user=user2, type='Strength', duration=45)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data'))