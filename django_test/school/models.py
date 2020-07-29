import uuid
from datetime import datetime

from django.core import validators
from django.db import models


class School(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified_at = models.DateTimeField(auto_now=True, null=True)
    name = models.CharField(max_length=20)
    students_max_number = models.IntegerField(default=100)

    # Additional fields
    established_in = models.IntegerField(validators=[  # In range [1900, <current_year>]
        validators.MinValueValidator(1900),
        validators.MaxValueValidator(datetime.now().year)])
    location = models.CharField(max_length=50)

    def save(self, *args, **kwargs):
        if self.established_in < 1900 or self.established_in > datetime.now().year:
            raise ValueError(f'established_in value must be in range [1900, {datetime.now().year}')
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.name}({self.students_max_number})'


class Student(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified_at = models.DateTimeField(auto_now=True, null=True)
    student_id = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    school = models.ForeignKey(School, on_delete=models.CASCADE)

    # Additional fields
    date_of_birth = models.DateField()
    nationality = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.student_id}: {self.first_name} {self.last_name}'

    @staticmethod
    def __generate_id(length=20):
        generated_id = uuid.uuid4().hex[:length]
        while Student.objects.filter(student_id=generated_id).count() > 0:
            generated_id = uuid.uuid4().hex[:length]

        return generated_id

    def save(self, *args, **kwargs):

        if self._state.adding:
            students_count = Student.objects.filter(school=self.school).count()

            if students_count >= self.school.students_max_number:
                raise ValueError('Maximum number of students exceed')

            self.student_id = self.__generate_id()

        super().save(*args, **kwargs)

