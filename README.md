# ResumeDjango
Fake Data CSV Generator (Django, Celery)

Web generator of CSV files with fake data

Demo

Live demo of project you may check here - https://csvfaker.herokuapp.com/

Login: test
Password: test

Description

Online service for generating CSV files with fake (dummy) data, developed with Python and Django.

App lets you create .CSV file with data of choice. You may choose type of data, text of headers, order of columns and number of rows.
This scheme may be later generated into .CSV file and downloaded.

Task of file generation is handled via Celery, and code of task is stored at dummy_gen/tasks.py.

Built with

Django - The web framework used
Celery - Distributing of tasks
Heroku Redis - Brocker
Faker - Generator of data for .CSV files
Celery progress and Django celery results- for task progress tracking and task results storing, respectively
AWS S3 - Storing generated .CSV files
Whitenoise - Static files management
ElaAdmin Template - Bootstrap template
