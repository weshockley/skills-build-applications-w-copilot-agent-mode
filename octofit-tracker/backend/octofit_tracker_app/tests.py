from django.test import TestCase
from .models import UserProfile, Team, Activity, Workout, Leaderboard

class UserProfileModelTest(TestCase):
    def test_create_user(self):
        user = UserProfile.objects.create(username='testuser', email='test@example.com', first_name='Test', last_name='User')
        self.assertEqual(user.username, 'testuser')

class TeamModelTest(TestCase):
    def test_create_team(self):
        user = UserProfile.objects.create(username='testuser2', email='test2@example.com', first_name='Test', last_name='User')
        team = Team.objects.create(name='Test Team')
        team.members.add(user)
        self.assertEqual(team.name, 'Test Team')

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        user = UserProfile.objects.create(username='testuser3', email='test3@example.com', first_name='Test', last_name='User')
        activity = Activity.objects.create(user=user, activity_type='run', duration_minutes=30, points=10, date='2025-05-01')
        self.assertEqual(activity.activity_type, 'run')

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        user = UserProfile.objects.create(username='testuser4', email='test4@example.com', first_name='Test', last_name='User')
        workout = Workout.objects.create(name='Morning Run', description='A quick run', suggested_by=user)
        self.assertEqual(workout.name, 'Morning Run')

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard(self):
        user = UserProfile.objects.create(username='testuser5', email='test5@example.com', first_name='Test', last_name='User')
        leaderboard = Leaderboard.objects.create(user=user, total_points=100)
        self.assertEqual(leaderboard.total_points, 100)
