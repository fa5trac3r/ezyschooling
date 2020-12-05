## Frontend Setup
No additional setup is required for frontend of the application just launch index.html file.

## Database Setup
Below is a great article on setting up postgres in windows.
https://medium.com/@9cv9official/creating-a-django-web-application-with-a-postgresql-database-on-windows-c1eea38fe294

* Install postgres in your pc
* During setup set password if asked as “password” and username as “postgres”
* If asks for port to run postgres set it to “5432”
Download and launch pgadmin4 .
* In the pgadmin databases create a new database
With the name 'ezyschooling'
* With this database part is done.



## Backend Setup
* First start with installing python on your pc.
* Then pip install virtualenv.
* Clone the repository 
* Start the terminal at this current directory and run commands like
```bash
$ virtualenv env 
$ source env/bin/activate on linux/mac
       OR
$ env/scripts/activate  on windows
(env) $ pip install -r requirements.txt
(env) $ python manage.py migrate
(env) $ python manage.py runserver
```

## Api Endpoints
* /api/pizzas
    - GET- gives list of all the available pizzas with name, size, type, topping
    - POST- creates a new pizza with name, size, type, topping
    - PUT- used to edit an already present pizza
    - DELETE- used to delete a particular pizza
* /api/pizzas/sizes
    - GET- gives list of all the sizes of pizzas available with id and name
    - POST - creates a new size of pizza with provided name
* /api/pizzas/toppings
    - GET- gives list of all the toppings of pizzas available with id and name
    - POST - creates a new topping of pizza with provided name