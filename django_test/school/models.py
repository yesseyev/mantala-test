import uuid

from django.db import models


class School(models.Model):
    name = models.CharField(max_length=20)
    students_max_number = models.IntegerField(default=100)

    def __str__(self):
        return f'{self.name}({self.students_max_number})'


class Student(models.Model):
    student_id = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    school = models.ForeignKey(School, on_delete=models.CASCADE)

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

