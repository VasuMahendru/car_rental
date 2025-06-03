# rental/serializers.py

from rest_framework import serializers
from .models import Car, Booking, Feedback
from django.contrib.auth.models import User

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    car = CarSerializer()

    class Meta:
        model = Booking
        fields = '__all__'

class FeedbackSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = Feedback
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']
