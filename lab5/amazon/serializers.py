from dataclasses import field
from django.contrib.auth.models import User, Group
from rest_framework import serializers

from .models import Student, Track, Intake 


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student 
        fields = ['id', 'name', 'age', 'notes', 'track', 'intake']


class TrackSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Track 
        fields = ['name', 'description']


class IntakeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Intake 
        fields = ['intake_no', 'start_date', 'end_date']


    