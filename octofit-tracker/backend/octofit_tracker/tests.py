from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create(email='test@hero.com', name='Test Hero', team='Marvel')
        self.assertEqual(user.name, 'Test Hero')

class TeamModelTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name='Avengers')
        self.assertEqual(team.name, 'Avengers')

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        activity = Activity.objects.create(user='Test Hero', activity_type='Running', duration=10)
        self.assertEqual(activity.activity_type, 'Running')

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard(self):
        entry = Leaderboard.objects.create(user='Test Hero', points=50)
        self.assertEqual(entry.points, 50)

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        workout = Workout.objects.create(name='Pushups', description='Do 20 pushups')
        self.assertEqual(workout.name, 'Pushups')
