# Django-Rest-Framework-API-Tutorials

## API's using DRF 
### Tech Stacks
Install the following required packages/modules using pip
```bash
pip install django djangorestframework
```
After the packages installing successfully, use the below command to create project
```bash
django-admin startproject drf_api_project_folder .
```
The above code will create a project folder named `drf_api_project_folder`. I am going to create two applications `1. mainApp` and `2. helloWorld` by using the below command
### 1. mainApp
```bash
python manage.py startapp mainApp
```
### 2. helloWorld
```bash
python manage.py startapp helloWorld
```
Okay, so let's move into the next section, after successfully create apps, need to add into `INSTALLED_APPS` on `settings.py` file in the project folder.
```
#settings.py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'helloWorld',
    'mainApp'
]
```
## mainApp
`mainApp` will navigate the user about the end-points and other operations
## helloWorld 
`helloWorld` app just an application to demonstrate the basic api operations
On the day ```02.04.2024``` on hello world app we create a sample model and other sample views to display data on JSON format



