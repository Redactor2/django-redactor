# django-redactor
Django Module for Redactor

To try this, add <var>static</var> folder to <var>redactorjs</var> folder, and place your Redactor II files into <var>redactor</var> directory within this static folder. To get Redactor II, visit https://imperavi.com/redactor.

## Requirements

See requirements.txt:

- Django==1.9.7
- image==1.5.3
- Pillow==3.2.0

## Test

Simple way to run:

```
pip install -r requirements.txt
./manage.py migrate
./manage.py runserver
```
Go to http://localhost:8000
