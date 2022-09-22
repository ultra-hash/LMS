# LMS - Library management system: 

 

## Overview: 

To manage and organize the books and to view the availability of the books. An admin can login and register books in the database. The available books can be viewed by the students from the home page. Admins can register and login to perform create, update, retrieve and delete operations. This project is built upon python’s Django framework.

 

## Installation: 

    Pre-requirements:  Python 3.7 and above  

### Step 1: clone Git repo 

    Git clone https://github.com/ultra-hash/LMS.git 

### Step 2: create virtual environment – optional 

For Linux / mac

    python3 -m venv venv 

	Source ./venv/bin/activate 


For windows 

	python -m venv venv 

	.\venv\Scripts\activate 

### Step 3: install dependencies  

	pip –r install requirements.txt 

or 

	Pip3 –r install requirements.txt 

### Step 4: Database Setup 

	In the Main Project’s [LMS] / [setting.py] file configure your own database credentials. For more details visit Django framework documentation 

setting.py 

    # configure with your own credentials
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'swamy_db',
            'USER': 'swamy',
            'PASSWORD': 'supersecretpassword', # change me 
            'HOST': 'mysql.st-site.tk',
            'PORT': 3306,
            
        }
    }

 
### Setup 5: Run the app 

From the work directory where manage.py resides.And run 
    
    python3 manage.py runserver 

 

 

This Django Project is compartmentalized with Django apps. Each app has is own purpose to support our project. 

 

LMS – main project folder 

Books – app 

Login – app 

Static – static files directory 

 

# Books App - function is to view, create, update, delete records of the books.
-   logged in user can create , update, list and delete records of the books.
-   The student can only list/view the records of the books. 

## Views.py File

### create view:

    def create(request): 
        if not verify_login(request): 
            return redirect('login.login') 
    
        if request.method == 'POST': 
            title = request.POST['title'] 
            if title == "" or title == None: 
                messages.info(request, "Title can't be empty") 
                return redirect('books.create') 
            book = books.objects.create(title=title) 
            messages.info(request, f"{title} book added successfully") 
            return redirect("books.list") 
        else: 
            return render(request, "books/books_form.html", {'login': verify_login(request)}) 
 

when create view called it can perform 2 types of tasks based on request type

Get Request 

-   When the create view gets a `GET request` it returns a form. The form contains the field to add title of the book to database.  

Post Request 

-   When the create view gets a `POST request` it validates the content received through the POST request and adds it to the database. After that it redirects to the domain.com/books/list .

 
### Update view:

    http://example.com/books/update/pk  # here pk refers to primary key of book from the database

function : 

    def update(request, pk): 
        if not verify_login(request): 
            return redirect('login.login') 
    
        if books.objects.filter(pk=pk).exists(): 
            book = books.objects.get(pk=pk) 
        else: 
            messages.info(request, f"book doesn't exists") 
            return redirect('books.list') 
    
        if request.method == 'POST': 
            newTitle = request.POST['title'] 
            prev = book.title 
            book.title = newTitle 
            book.save() 
            messages.success(request, f"{prev} book updated to {newTitle} successfully") 
            return redirect('books.list') 
        else: 
            return render(request, "books/books_form.html", {'book':book, 'login':verify_login(request)}) 

 
Just like create view, update view also performs 2 tasks based on request type.  

GET request 
- will return a form to update a specific book which will be retrieved from the database by the help of additional attribute pk = primary key. 
 
POST request 
-   The `post request` is performed from the form obtined from the `GET request` will update the title of the book by overwriting the existing title of the book in the database. 

 
### Delete views:  

    http://example.com/books/delete/pk # here pk referes to primary key of book from the database

function:

    def delete(request, pk): 
        if not verify_login(request): 
            return redirect('login.login') 
            
        if books.objects.filter(pk=pk).exists(): 
            book = books.objects.get(pk=pk) 
            book.delete() 
        else: 
            messages.info(request, f"book doesn't exists") 
        return redirect("books.list") 

 

-   This function's objective is to delete the books from the database. This function doesn’t want any specific request type. Once the request received, it will check if the book exists or not with the specified primary key, if exists it will delete from the database. 

 
### List view: 

    def list(request):
        login = verify_login(request) 
        list_books = books.objects.all() 
        return render(request, "books/books_list.html", {'list_books': list_books, 'login': login}) 

-   This function doesn’t have any restrictions. Students can view this page. This view will display all the books available in the database. 

-   If this is viewed by admin while logged in, admin can update, delete specific entries and create new entry of the books. 

# Login – app function is to provide authentication and authorization  

view.py

### login view: 
    
    http://example.com/login

function:

    def login(request):
    if verify_login(request):
        return redirect('books.list')

    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        if adminAccounts.objects.filter(email=email, password=password).exists():
            admin = adminAccounts.objects.get(email=email, password=password)
            request.session['login'] = True
            messages.success(request, "login successfull")
            return redirect('books.list')
        else:
            messages.info(request, "Email and Password don't match.")
            return redirect('login.login')
    else:
        return render(request, "login/login.html", {})

This function performs 2 tasks according to request received.

GET REQUEST:
-   When GET request received it will return a form to enter email and password to login to the application

POST REQUEST:
-   When POST request received, it will recieve the email and password credentials  from FORM. And verifies the obtined credientials against the database. if credentials match a session variable is created ``request.session['login'] = True`` is created and it will redirect you to `example.com/books/list` else returns to the login page with message 'email and password doesn't match'



### register view:

    http://example.com/register

function:

    def register(request):
        if verify_login(request):
            return redirect('books.list')
            
        if request.method == 'POST':
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']

            if not adminAccounts.objects.filter(email=email).exists():
                admin = adminAccounts.objects.create(username=username, email=email, password=password)
                messages.success(request, "account created successfully")
                return redirect('login.login')
            else:
                messages.info(request, "email already registered")
                return redirect('login.register')
        else:
            return render(request, "login/register.html", {})

This function performs 2 tasks according to request received.

GET REQUEST:
-   When GET request received it will return a form to enter username , email and password to register/signup

POST REQUEST:
-   When a POST request received, it will recieve the username, email and password credentials  from FORM. And verifies if email already used or not, aginest the database. if email not in the database it will redirect you to `example.com/login/` else returns to register page with message 'email already exists'

### logout view:

    http://example.com/logout

function:

    def logout(request):
    try:
        if request.session['login']:
            del request.session['login']
            messages.info(request, "logout successfull")
    except KeyError:
        pass
    finally:
        return redirect('books.list')


-   This function objective is to delete the `request.session['login']`. If user not logged in and tried to visit this logout view. The `request.session['login']` will through a `KeyError`. so this code is written in a try block. if a logged in user tried to logout the then will run without any `KeyError` hence the `request.session['login']` is deleted and added message to messages  framework saying ` logout successful `.

### verify_code view:

-   This view not view which is accessible by the outside world. It is for internal access only.
-   This function returns True or False only.

function:

    # return True or False
    def verify_login(request):
        try:
            if request.session['login']:
                return True
        except KeyError:
            return False

-   Just like logout, but it checks if the `request.session['login']` variable exists or not. If exists, it return True else it return False



# Static – which holds the static files for this project 

Static / templates directory contsists of templates for hole project

templates for each app is located in its own app directory like 

    ./books
        ./templates
            ./books
                books_form.html
                books_list.html

    ./login
        ./templates
            ./login
                login.html
                register.html

    ./LMS
        no files here

    ./static
        ./templates
            base.html

# Models

## books app
### models.py

    from django.db import models

    class books(models.Model):
        title = models.CharField(max_length=40)


-   models are the django ORM - object relational mapper/mapping which interacts with the database. It is responsible for creating and setting up database tables.

-   The above class creates a table named `books` with columns with the variables mentioned in class i.e., title in the database.

## login app
### models.py

    from django.db import models

    class adminAccounts(models.Model):
        username = models.CharField(max_length=20)
        email = models.EmailField(max_length=256)
        password = models.CharField(max_length=256)

-   The above class creates a table named `adminAccounts` with columns with the variables mentioned in class i.e., username, email, password in the database.


# URLS

-   each urlpatterns represents or directs to a specific page
-   naming convenstion followed here for name of path is `[appname].[view name]`
-   each app's url.py file should be inlucded in the main project's url.py file

## LMS - main project folder

### urls.py

    from django.contrib import admin
    from django.urls import path, include

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('books/', include('books.urls')),
        path('', include('login.urls')),
    ]

-   include method is used to achieve this clean view else you can directly mention each url of each apps url path here. But it is not best practice.

## books app

### urls.py

    from django.urls import path
    from . import views

    urlpatterns = [
        path('', views.index, name="books.index"),
        path('create/', views.create, name="books.create"),
        path('list/', views.list, name="books.list"),
        path('update/<pk>', views.update, name="books.update"),
        path('delete/<pk>', views.delete, name="books.delete"),
    ]


## login app
### urls.py

    from django.urls import path
    from . import views

    urlpatterns = [
        path('login/', views.login, name="login.login"),
        path('logout/', views.logout, name="login.logout"),
        path('register/', views.register, name="login.register"),
        path('', views.index, name="login.index"),
    ]


## additional information

visit [django website](https://www.djangoproject.com/)