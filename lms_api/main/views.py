from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import TeacherSerializer
from rest_framework.response import Response
from rest_framework import generics
from .models import (Teacher, Course, CourseCategory, Student)
# Create your views here.

# class TeacherList(APIView):

#     def get(self, request):
#         teachers = Teacher.objects.all()
#         serializer = TeacherSerializer(teachers, many=True)
#         return Response(serializer.data)
""" Create/Post Method """


class TeacherList(generics.ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class TeacherDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
