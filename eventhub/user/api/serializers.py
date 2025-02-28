from rest_framework import serializers
from event.models import Event

class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'