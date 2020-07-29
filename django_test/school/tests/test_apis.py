import random

from django.test import TestCase
from faker import Faker
from rest_framework import status
from rest_framework.test import APIClient

from school.models import School, Student


class SchoolAPITests(TestCase):
    """ Test module for School model """

    def setUp(self) -> None:
        """ Initial database setup with N (schools_count) schools """
        self.schools_count = 5
        self.fake = Faker()

        self.schools = [
            School.objects.create(
                name=f'{self.fake.last_name()[:10]}\'s school',
                students_max_number=1000,
                established_in=2020,
                location=self.fake.street_address()
            ) for _ in range(self.schools_count)]

    def test_api_list(self):
        """ List API ( /schools/ ) """
        client = APIClient()
        response = client.get('/schools/')

        # Status check
        self.assertEquals(response.status_code, status.HTTP_200_OK)

        # Count check
        self.assertEquals(response.data['count'], School.objects.count())

        # Fetched elements size check
        self.assertEquals(len(response.data['results']), self.schools_count)

    def test_api_post(self):
        """ POST API ( /schools/ ) """
        client = APIClient()
        school_data = {
            'name': f'{self.fake.last_name()[:10]}\'s school',
            'students_max_number': 100,
            'established_in': 1996,
            'location': self.fake.street_address(),
        }

        response = client.post('/schools/', school_data, format='json')

        # Status check
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

        # Overall count check
        self.assertEquals(School.objects.count(), self.schools_count + 1)

        # Post data check
        for key, val in school_data.items():
            self.assertEquals(response.data[key], val)

    def test_api_get(self):
        """ GET API ( /schools/<int:pk> ) """
        client = APIClient()
        school = self.schools[1]

        response = client.get(f'/schools/{school.pk}/')

        # Status check
        self.assertEquals(response.status_code, status.HTTP_200_OK)

        # Comparing saved instance and retrieved record fields
        self.assertEquals(school.name, response.data['name'])
        self.assertEquals(school.students_max_number, response.data['students_max_number'])
        self.assertEquals(school.established_in, response.data['established_in'])
        self.assertEquals(school.location, response.data['location'])

    def test_api_put(self):
        """ PUT API ( /schools/<int:pk> ) """
        client = APIClient()
        school = self.schools[0]

        school_data = {
            'name': school.name,
            'established_in': 2000,
            'location': school.location + ' updated',
        }

        response = client.put(f'/schools/{school.pk}/', school_data, format='json')

        # Status check
        self.assertEquals(response.status_code, status.HTTP_200_OK)

        # Retrieving updated school from db
        school_db = School.objects.get(pk=school.pk)

        # Updated fields comparison
        self.assertEquals(school_db.established_in, school_data['established_in'])
        self.assertEquals(school_db.location, school_data['location'])

    def test_api_delete(self):
        """ DELETE API ( /schools/<int:pk> ) """

        client = APIClient()
        school = self.schools[2]

        response = client.delete(f'/schools/{school.pk}/')

        # Status check
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)

        # Checking that record deleted from db
        with self.assertRaises(School.DoesNotExist):
            school_db = School.objects.get(pk=school.pk)


class StudentAPITests(TestCase):
    """ Test module for School model """

    def setUp(self) -> None:
        """ Initial database setup with N (schools_count) schools """
        self.students_count = 10
        self.fake = Faker()
        self.school = School.objects.create(
            name=f'{self.fake.last_name()[:10]}\'s school',
            students_max_number=1000,
            established_in=2020,
            location=self.fake.street_address()
        )

        self.students = [
            Student.objects.create(
                first_name=self.fake.first_name()[:20],
                last_name=self.fake.last_name()[:20],
                school=self.school,
                date_of_birth=self.fake.date_of_birth(),
                nationality=self.fake.country()[:20]
            ) for _ in range(self.students_count)]

    def test_api_list(self):
        """ List API ( /students/ ) """
        client = APIClient()
        response = client.get('/students/')

        # Status check
        self.assertEquals(response.status_code, status.HTTP_200_OK)

        # Count check
        self.assertEquals(response.data['count'], Student.objects.count())

        # Fetched elements size check
        self.assertEquals(len(response.data['results']), self.students_count)

    def test_api_post(self):
        """ POST API ( /students/ ) """
        client = APIClient()
        student_data = {
            'first_name': self.fake.first_name()[:20],
            'last_name': self.fake.last_name()[:20],
            'school': self.school.pk,
            'date_of_birth': self.fake.date_of_birth(),
            'nationality': self.fake.country()[:20]
        }

        response = client.post('/students/', student_data, format='json')

        # Status check
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

        # Overall count check
        self.assertEquals(Student.objects.count(), self.students_count + 1)

        # Student id length check (20 chars)
        self.assertEquals(len(response.data['student_id']), 20)

        # Post data check
        for key, val in student_data.items():
            self.assertEquals(str(response.data[key]), str(val))

    def test_api_get(self):
        """ GET API ( /students/<int:pk> ) """
        client = APIClient()
        student = self.students[1]

        response = client.get(f'/students/{student.pk}/')

        # Status check
        self.assertEquals(response.status_code, status.HTTP_200_OK)

        # Comparing saved instance and retrieved record fields
        self.assertEquals(student.first_name, response.data['first_name'])
        self.assertEquals(student.last_name, response.data['last_name'])
        self.assertEquals(student.student_id, response.data['student_id'])
        self.assertEquals(student.nationality, response.data['nationality'])
        self.assertEquals(str(student.date_of_birth), response.data['date_of_birth'])

    def test_api_put(self):
        """ PUT API ( /students/<int:pk> ) """
        client = APIClient()
        student = self.students[0]

        student_data = {
            'first_name': student.first_name,
            'last_name': self.fake.last_name()[:20],  # Updated
            'nationality': student.nationality,
            'date_of_birth': self.fake.date_of_birth(),
            'school': student.school.pk,
        }

        response = client.put(f'/students/{student.pk}/', student_data, format='json')

        # Status check
        self.assertEquals(response.status_code, status.HTTP_200_OK)

        # Retrieving updated school from db
        student_db = Student.objects.get(pk=student.pk)

        # Updated fields comparison
        self.assertEquals(student_db.last_name, student_data['last_name'])
        self.assertEquals(student_db.date_of_birth, student_data['date_of_birth'])

    def test_api_delete(self):
        """ DELETE API ( /students/<int:pk> ) """

        client = APIClient()
        student = self.students[2]

        response = client.delete(f'/students/{student.pk}/')

        # Status check
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)

        # Checking that record deleted from db
        with self.assertRaises(Student.DoesNotExist):
            student_db = Student.objects.get(pk=student.pk)


class NestedAPITests(TestCase):
    """ Test module for School model """

    def setUp(self) -> None:
        """ Initial database setup with N (schools_count) schools """
        self.schools_count = 5
        self.students_count = 100
        self.fake = Faker()

        self.schools = [
            School.objects.create(
                name=f'{self.fake.last_name()[:10]}\'s school',
                students_max_number=1000,
                established_in=2020,
                location=self.fake.street_address()
            ) for _ in range(self.schools_count)]

        self.students = [
            Student.objects.create(
                first_name=self.fake.first_name()[:20],
                last_name=self.fake.last_name()[:20],
                school=self.schools[random.randrange(self.schools_count)],
                date_of_birth=self.fake.date_of_birth(),
                nationality=self.fake.country()[:20]
            ) for _ in range(self.students_count)]

    def test_api_list(self):
        """ List API ( /schools/<int:school_pk>/students/ ) """
        school = self.schools[0]
        client = APIClient()
        response = client.get(f'/schools/{school.pk}/students/')

        # Status check
        self.assertEquals(response.status_code, status.HTTP_200_OK)

        # Count check
        self.assertEquals(response.data['count'], Student.objects.filter(school=school).count())

    def test_api_post(self):
        """ POST API ( /schools/<int:school_pk>/students/ ) """
        student_data = {
            'first_name': self.fake.first_name()[:20],
            'last_name': self.fake.last_name()[:20],
            'school': self.schools[0].pk,
            'date_of_birth': self.fake.date_of_birth(),
            'nationality': self.fake.country()[:20]
        }

        client = APIClient()
        response = client.post(f'/schools/{self.schools[0].pk}/students/', student_data, format='json')

        # Status check
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

        # Student id length check (20 chars)
        self.assertEquals(len(response.data['student_id']), 20)

        # Post data check
        for key, val in student_data.items():
            self.assertEquals(str(response.data[key]), str(val))

    def test_api_get(self):
        """ GET API ( /schools/<int:school_pk>/students/<int:student_pk> ) """
        student = self.students[0]

        client = APIClient()
        response = client.get(f'/schools/{student.school.pk}/students/{student.pk}/')

        # Status check
        self.assertEquals(response.status_code, status.HTTP_200_OK)

        # Comparing saved instance and retrieved record fields
        self.assertEquals(student.first_name, response.data['first_name'])
        self.assertEquals(student.last_name, response.data['last_name'])
        self.assertEquals(student.student_id, response.data['student_id'])
        self.assertEquals(student.nationality, response.data['nationality'])
        self.assertEquals(str(student.date_of_birth), response.data['date_of_birth'])

    def test_api_put(self):
        """ PUT API ( /schools/<int:school_pk>/students/<int:student_pk> ) """
        client = APIClient()
        student = self.students[0]

        student_data = {
            'first_name': student.first_name,
            'last_name': self.fake.last_name()[:20],  # Updated
            'nationality': student.nationality,
            'date_of_birth': self.fake.date_of_birth(),
            'school': student.school.pk,
        }

        response = client.put(f'/schools/{student.school.pk}/students/{student.pk}/', student_data, format='json')

        # Status check
        self.assertEquals(response.status_code, status.HTTP_200_OK)

        # Retrieving updated school from db
        student_db = Student.objects.get(pk=student.pk)

        # Updated fields comparison
        self.assertEquals(student_db.last_name, student_data['last_name'])
        self.assertEquals(student_db.date_of_birth, student_data['date_of_birth'])

    def test_api_delete(self):
        """ DELETE API ( /schools/<int:school_pk>/students/<int:student_pk> ) """

        client = APIClient()
        student = self.students[2]

        response = client.delete(f'/schools/{student.school.pk}/students/{student.pk}/')

        # Status check
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)

        # Checking that record deleted from db
        with self.assertRaises(Student.DoesNotExist):
            student_db = Student.objects.get(pk=student.pk)
