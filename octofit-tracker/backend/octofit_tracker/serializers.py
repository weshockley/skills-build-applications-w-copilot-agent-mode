from rest_framework import serializers
from .models import UserProfile, Team, Activity, Workout, Leaderboard

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

class TeamSerializer(serializers.ModelSerializer):
    members = UserProfileSerializer(many=True, read_only=True)
    class Meta:
        model = Team
        fields = '__all__'

class ActivitySerializer(serializers.ModelSerializer):
    user = UserProfileSerializer(read_only=True)
    class Meta:
        model = Activity
        fields = '__all__'

class WorkoutSerializer(serializers.ModelSerializer):
    suggested_by = UserProfileSerializer(read_only=True)
    class Meta:
        model = Workout
        fields = '__all__'

class LeaderboardSerializer(serializers.ModelSerializer):
    user = UserProfileSerializer(read_only=True)
    class Meta:
        model = Leaderboard
        fields = '__all__'
