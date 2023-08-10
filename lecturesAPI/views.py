from django.shortcuts import render
from rest_framework.response import Response
from lecturesAPI.models import Lecture
from lecturesAPI.serializer import LectureSerializer
from rest_framework.decorators import api_view
 
@api_view(['POST'])
def lecture_create(request):
    serializer = LectureSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)
    
@api_view(['GET'])
def lecture_list(request):
    lectures = Lecture.objects.all() #complex data
    serializer = LectureSerializer(lectures, many=True)
    return Response(serializer.data)

@api_view(['GET', 'PUT', 'DELETE'])
def lecture(request, pk):
    lecture = Lecture.objects.get(pk=pk)
    if request.method == 'GET':
        serializer = LectureSerializer(lecture)
        return Response(serializer.data)
    if request.method == 'PUT':
        serializer = LectureSerializer(lecture, data=request.data)
        return Response(serializer.data)
