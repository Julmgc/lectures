from rest_framework import serializers
from lecturesAPI.models import Lecture

class LectureSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    subject = serializers.CharField()
    lecturer = serializers.CharField()
    place = serializers.CharField()
    date_time = serializers.DateTimeField()
    audience = serializers.IntegerField()

    def create(self, data): 
        return Lecture.objects.create(**data)
    

