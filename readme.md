# [Dummy Api](https://django-restql.yezyilomo.com)
this is a demo api project in order to demostrate how the django rest api works. it contains a user authentication system (signup, signin, signout) and a mini blog.

## Features
* Basic Http Authentication (Token based)
* GraphQL like api queries
* Api Documentation (Redoc and swagger)
* Full Api Meta

## Usage
    1 git clone ......
    2 create virtual environmrnt on your local machine and activate
    3  inside project's root directory run "pip install -r requirements.txt"
    4. run "python manage.py migrate"
    5. run "python manage.py runserver"
    6. Goto your browser visit "127.0.0.1"
    7. you've got yourself a working project hahaha

### Api Queries
append query params to GET requests to control amount of data return on your request

1. this returns only the id and title of the articles 

        GET /articles/?query={id, title}

2. nested queries: return specific fields from a nested fields

        GET /articles/?query={title, comments{id}}
3. exclude specific fields from a database query

        GET /articles/?query={-id}
