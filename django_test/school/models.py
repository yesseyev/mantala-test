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

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        # TODO: generate unique student_id (20 chars)
        pass
