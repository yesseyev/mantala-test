#Solutions for Mantala challenges:

##Python
* **Exercise 1**: Object Oriented Programming ([solution](python_ex_1/answer.py) | [test](python_ex_1/tests.py)) 
* **Exercise 2**: Randomness Test ([solution](python_ex_2/answer.py) | [test](python_ex_2/tests.py)) 
* **Exercise 3**: Algorithmic Test ([solution](python_ex_3/answer.py) | [test](python_ex_3/tests.py)) 
* **Exercise 4**: Scraping Test ([solution](python_ex_4/answer.py) | [test](python_ex_4/tests.py)) 


## Django
* **PostgreSQL** is used as database
* **Pipenv** dependency manager added
* Sensitive information stored in .env file (loaded using **python-dotenv**)
* Models meets all requirements and additional `created_at`, `last_modified_at` system datetime fields were added.
* [BONUS] **School** model has extra `established_in`, `location` fields 
* [BONUS] **Student** model has extra `date_of_birth`, `nationality` fields 
* REST API was realized with usage of `ModelViewSet` and `ModelSerializer`
* Unique student_id string generation added
* `Maximum number of students` limit implemented for both domain and nested Student creation
* `drf-nested-routers` implemented with all corresponding logic
* [BONUS] Search and Ordering filters added
* [BONUS] Pagination added (PageNumberPagination) with default page_size=10
* [BONUS] Data population with Faker added. `python manage.py populate_db` ()
* [IN PROCESS] Test coverage
* [IN PROCESS] Heroku deployment