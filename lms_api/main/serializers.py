from rest_framework import serializers
from .models import (Teacher, CourseCategory, Course, Student)


class TeacherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Teacher
        fields = [
            "id", "full_name", "email", "password", "qualification", "mobile",
            "address"
        ]
