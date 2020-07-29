from rest_framework import serializers
from .models import School, Student


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ['id', 'created_at', 'name', 'students_max_number', 'established_in', 'location']
        read_only_fields = ('created_at',)


class SchoolSerializerWithoutStudentsMaxNumber(serializers.ModelSerializer):
    """ Extra serializer for PUT request (write_once for students_max_number) """
    class Meta:
        model = School
        fields = ['id', 'created_at', 'name', 'students_max_number', 'established_in', 'location']
        read_only_fields = ('students_max_number', 'created_at',)


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'created_at', 'student_id', 'first_name', 'last_name', 'school', 'date_of_birth', 'nationality']
        read_only_fields = ('student_id', 'created_at',)

