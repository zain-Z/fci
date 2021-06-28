from rest_framework import serializers
from .models import FinalResult


class FinalResultSerializer(serializers.ModelSerializer):

    class Meta:
        model = FinalResult
        fields = [
            'course',
            'student',
            'results',
        ]
