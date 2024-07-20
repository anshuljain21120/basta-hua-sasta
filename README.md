# Basta Hua Sasta

Steps to run:

[//]: # (https://bootstrap-ecommerce.com/)

Install dependencies
```shell
pip install -r requirements.txt
```
Create schema
```shell
python manage.py makemigrations
```
Create Tables
```shell
python manage.py migrate
```
Populate Data in tables
```shell
python manage.py runscript populate_initial_data
```
Finally, start server
```shell
python manage.py runserver
```
