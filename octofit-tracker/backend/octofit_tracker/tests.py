from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class ModelTests(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Test Team')
        self.user = User.objects.create(name='Test User', email='test@example.com', team=self.team)
        self.workout = Workout.objects.create(name='Test Workout', description='Test Desc')
        self.activity = Activity.objects.create(user=self.user, type='Run', duration=10, calories=100)
        self.leaderboard = Leaderboard.objects.create(user=self.user, score=123)

    def test_user_created(self):
        self.assertEqual(User.objects.count(), 1)

    def test_team_created(self):
        self.assertEqual(Team.objects.count(), 1)

    def test_activity_created(self):
        self.assertEqual(Activity.objects.count(), 1)

    def test_workout_created(self):
        self.assertEqual(Workout.objects.count(), 1)

    def test_leaderboard_created(self):
        self.assertEqual(Leaderboard.objects.count(), 1)
