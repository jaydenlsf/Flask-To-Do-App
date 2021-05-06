# First QA Mini Project - Flask To-Do App

## Introduction

A very simple to-do list web application created using Flask, SQLAlchemy, WTForms and Jinja2.

## Installation

To install the required dependencies:

```
$ pip3 install -r requirements.txt
```

## Instruction

In order for the application to run, set your environment variables for `DATABASE_URI` and `SECRET_KEY`.<br/>
`DATABASE_URI` is in the format of `'mysql+pymysql://root:testpass@localhost/testdb'` and `SECRET_KEY` can be anything.<br/><br/>

After the variables are set, initialise an empty table within the database by running:

```
$ python3 create.py
```

To run the app:

```
$ flask run
```

## Demo

### Homepage (without any tasks)

![homepage1](https://user-images.githubusercontent.com/54101378/117377894-3b840000-aecc-11eb-8df4-a4eefb4400e6.png)

### Homepage (with tasks created)

![homepage2](https://user-images.githubusercontent.com/54101378/117377911-48a0ef00-aecc-11eb-8a96-c3000c7ffbdf.png)

### Add Task Page

![add-task](https://user-images.githubusercontent.com/54101378/117377952-5787a180-aecc-11eb-834f-fc825fb6a22c.png)

### Edit Task Page

![edit-task](https://user-images.githubusercontent.com/54101378/117377974-5fdfdc80-aecc-11eb-9355-59decc264c18.png)
