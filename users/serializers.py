from rest_framework import serializers
from .models import Skill, UserProfile, User
from django.contrib.auth.models import User


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'

class UserProfileSerializer(serializers.ModelSerializer):
    skills = SkillSerializer(many=True)
    class Meta:
        model = UserProfile
        fields = ('age', 'phone_number', 'description', 'skills')


class UserSerializer(serializers.ModelSerializer):
    userprofile = UserProfileSerializer()
    class Meta:
        model = User
        fields = '__all__'