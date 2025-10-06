from rest_framework import serializers
from .models import Event, Sermon

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'  # Includes all fields: title, description, date, location, created_by, created_at

class SermonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sermon
        fields = '__all__'  # Includes all fields: title, preacher, content, date, created_at