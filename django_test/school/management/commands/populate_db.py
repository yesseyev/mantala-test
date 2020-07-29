from django.core.management.base import BaseCommand
from school.models import Student, School
from faker import Faker
import random


class Command(BaseCommand):
    args = ''
    help = 'Just populates database with Faker values'

    def _populate(self):
        fake = Faker()

        for _ in range(random.randint(10, 30)):
            school = School(
                name=f'{fake.last_name()[:10]}\'s school',
                students_max_number=random.randint(10, 200),
                established_in=random.randint(1900, 2020),
                location=fake.street_address()
            )
            school.save()
            for __ in range(random.randint(5, school.students_max_number)):
                student = Student(
                    first_name=fake.first_name()[:20],
                    last_name=fake.last_name()[:20],
                    school=school,
                    date_of_birth=fake.date_of_birth(),
                    nationality=fake.country()[:20]
                )
                student.save()

    def handle(self, *args, **options):
        self._populate()
