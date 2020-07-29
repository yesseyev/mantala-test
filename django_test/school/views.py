from rest_framework import viewsets, status, filters
from rest_framework.response import Response

from .models import School, Student
from .serializers import SchoolSerializer, StudentSerializer, SchoolSerializerWithoutStudentsMaxNumber


class SchoolModelViewSet(viewsets.ModelViewSet):
    serializer_class = SchoolSerializer
    queryset = School.objects.all()
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'location']
    ordering_fields = ['created_at', 'students_max_number', 'established_in']

    def get_serializer_class(self):
        """ Custom serializer class getter.
        In order to make students_max_number field "write_once"

        :return: serializer class depends on request method
        """
        serializer_class = self.serializer_class

        if self.request.method == 'PUT':
            serializer_class = SchoolSerializerWithoutStudentsMaxNumber

        return serializer_class


class StudentModelViewSet(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['student_id', 'first_name', 'last_name', 'nationality']
    ordering_fields = ['created_at', 'date_of_birth']

    def get_queryset(self):
        NESTED_PK = 'school_pk'
        if NESTED_PK in self.kwargs:
            return Student.objects.filter(school=self.kwargs[NESTED_PK])

        return super().get_queryset()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        except ValueError:
            return Response(['Maximum number of students exceeded'], status=status.HTTP_400_BAD_REQUEST)
