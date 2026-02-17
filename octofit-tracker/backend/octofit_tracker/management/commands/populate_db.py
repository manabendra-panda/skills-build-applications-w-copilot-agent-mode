from django.core.management.base import BaseCommand
from django.conf import settings
from djongo import models

class User(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    team = models.CharField(max_length=50)
    class Meta:
        app_label = 'octofit_tracker'

class Team(models.Model):
    name = models.CharField(max_length=50, unique=True)
    class Meta:
        app_label = 'octofit_tracker'

class Activity(models.Model):
    user = models.CharField(max_length=100)
    activity_type = models.CharField(max_length=50)
    duration = models.IntegerField()
    class Meta:
        app_label = 'octofit_tracker'

class Leaderboard(models.Model):
    user = models.CharField(max_length=100)
    points = models.IntegerField()
    class Meta:
        app_label = 'octofit_tracker'

class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    class Meta:
        app_label = 'octofit_tracker'

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        users = [
            User(email='ironman@marvel.com', name='Iron Man', team='Marvel'),
            User(email='captain@marvel.com', name='Captain America', team='Marvel'),
            User(email='spiderman@marvel.com', name='Spider-Man', team='Marvel'),
            User(email='batman@dc.com', name='Batman', team='DC'),
            User(email='superman@dc.com', name='Superman', team='DC'),
            User(email='wonderwoman@dc.com', name='Wonder Woman', team='DC'),
        ]
        for user in users:
            user.save()

        activities = [
            Activity(user='Iron Man', activity_type='Running', duration=30),
            Activity(user='Captain America', activity_type='Cycling', duration=45),
            Activity(user='Spider-Man', activity_type='Jumping', duration=20),
            Activity(user='Batman', activity_type='Swimming', duration=25),
            Activity(user='Superman', activity_type='Flying', duration=60),
            Activity(user='Wonder Woman', activity_type='Lifting', duration=35),
        ]
        for activity in activities:
            activity.save()

        leaderboard = [
            Leaderboard(user='Iron Man', points=100),
            Leaderboard(user='Captain America', points=90),
            Leaderboard(user='Spider-Man', points=80),
            Leaderboard(user='Batman', points=95),
            Leaderboard(user='Superman', points=110),
            Leaderboard(user='Wonder Woman', points=85),
        ]
        for entry in leaderboard:
            entry.save()

        workouts = [
            Workout(name='Pushups', description='Do 20 pushups'),
            Workout(name='Situps', description='Do 30 situps'),
            Workout(name='Squats', description='Do 40 squats'),
        ]
        for workout in workouts:
            workout.save()

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data'))
