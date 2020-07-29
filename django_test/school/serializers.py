from rest_framework import serializers
from .models import School, Student


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ['id', 'name', 'students_max_number']


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'student_id', 'first_name', 'last_name', 'school']
        read_only_fields = ('student_id',)

