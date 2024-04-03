# Django-Rest-Framework-API-Tutorials

## API's using DRF 
### Tech Stacks
Install the following required packages/modules using pip
```commandline
pip install django djangorestframework
```
After the packages installing successfully, use the below command to create project
```commandline
django-admin startproject drf_api_project_folder .
```
The above code will create a project folder named `drf_api_project_folder`. I am going to create two applications `1. mainApp` and `2. helloWorld` by using the below command
### 1. mainApp
```commandline
python manage.py startapp mainApp
```
### 2. helloWorld
```commandline
python manage.py startapp helloWorld
```
Okay, so let's move into the next section, after successfully create apps, need to add into `INSTALLED_APPS` on `settings.py` file in the project folder.
```python
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

## 03.04.2024 - ADMIN PANEL CONFIGURING
1. Changing Dash Board View

Changing the admin dashboard view from this

![img.png](img.png)

to this

![img_1.png](img_1.png)

by adding the code block on `admin.py` on your app folder, adding a new class in `admin.py` file like below

```python
class SampleAdmin(admin.ModelAdmin):
     list_display = ("id", "name", "age", "job", "created_at") #these names are the column names of our model
```

After adding the class you need to register on your admin site like below

```python
admin.site.register(Sample) #previous one only with model 
```
the above code needs to change to like below
```python
admin.site.register(Sample, SampleAdmin) 
```

2. Adding Links

Now you can view the data from dashboard and if you click the `id` it will navigate to the edit page, but if we need to do the same when we click other field like `name` to do that we are going to add an another attribute named `list_display_links` inside the class like below
```python
class SampleAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "age", "job", "created_at")
    list_display_links = ("id", "name")
```

3. Search Links

We can add search field using the same method, add a line of code like below
```python
class SampleAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "age", "job", "created_at")
    list_display_links = ("id", "name")
    search_fields = ("name", "job")
```
Always remember you need to provide column names on tuple always

4. Pagination

We can add pagination feature on our dashboard you can limit the table list per page, by adding the below line of code
```python
class SampleAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "age", "job", "created_at")
    list_display_links = ("id", "name")
    search_fields = ("name", "job")
    list_per_page = 10
```

5. Editing

We can implement the editing feature (without navigate to detail view) also, before that i am going to add an another boolean field on our model like below
```python
class Sample(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=0)
    job = models.CharField(max_length=100, null=True)
    is_active = models.BooleanField(default=True) #<--- Added field
    created_at = models.DateTimeField(default=datetime.now())
```
After the column added we need to run the scripts for `makemigrations` and `migrate` on our command prompt. After the migration we are going to add the `is_active` column for editable columns, like below
```python
class SampleAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "age", "job", "is_active", "created_at")
    list_display_links = ("id", "name")
    search_fields = ("name", "job")
    list_per_page = 10
    list_editable = ('is_active',)
```

6. Filter

Next we're going to add the filter option by using `list_filter` like below

```python
class SampleAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "age", "job", "is_active", "created_at")
    list_display_links = ("id", "name")
    search_fields = ("name", "job")
    list_per_page = 10
    list_editable = ('is_active',)
    list_filter = ("id", "name", "created_at")
```

After all these changes your admin dashboard will look like this

![img_3.png](img_3.png)









