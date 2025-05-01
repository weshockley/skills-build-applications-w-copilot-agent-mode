from django.core.management.base import BaseCommand
from octofit_tracker_app.models import UserProfile, Team, Activity, Workout, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data.'

    def handle(self, *args, **kwargs):
        # Clear existing data
        Leaderboard.objects.all().delete()
        Activity.objects.all().delete()
        Team.objects.all().delete()
        Workout.objects.all().delete()
        UserProfile.objects.all().delete()

        # Create users
        alice = UserProfile.objects.create(username='alice', email='alice@example.com', first_name='Alice', last_name='Smith')
        bob = UserProfile.objects.create(username='bob', email='bob@example.com', first_name='Bob', last_name='Brown')
        carol = UserProfile.objects.create(username='carol', email='carol@example.com', first_name='Carol', last_name='Jones')

        # Create teams
        team_alpha = Team.objects.create(name='Alpha')
        team_beta = Team.objects.create(name='Beta')
        team_alpha.members.add(alice, bob)
        team_beta.members.add(carol)

        # Create activities
        Activity.objects.create(user=alice, activity_type='run', duration_minutes=30, distance_km=5.0, points=50, date=timezone.now().date())
        Activity.objects.create(user=bob, activity_type='walk', duration_minutes=60, distance_km=4.0, points=40, date=timezone.now().date())
        Activity.objects.create(user=carol, activity_type='strength', duration_minutes=45, points=60, date=timezone.now().date())

        # Create workouts
        Workout.objects.create(name='Morning Run', description='A 5km run to start the day', suggested_by=alice)
        Workout.objects.create(name='Strength Circuit', description='Full body strength training', suggested_by=carol)

        # Create leaderboard
        Leaderboard.objects.create(user=alice, total_points=50)
        Leaderboard.objects.create(user=bob, total_points=40)
        Leaderboard.objects.create(user=carol, total_points=60)

        self.stdout.write(self.style.SUCCESS('Test data populated successfully.'))
