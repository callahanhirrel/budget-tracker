# BIRT: Budgets In Real Time

## Description

A [Flask](http://flask.pocoo.org/) application designed for real time tracking of budgets and funding for college/university academic departments.

This application is primarily intended to be used by administrative assistants, department chairs, and department professors.

Big user goals include:
* viewing funding distribution for a department in *real time*
* access to an archive of budget data to make predictions and be prepared for cyclic expenses
* editing database itself, adding, removing, editing fields

Other long term goals include development of an API and mobile-frontend to allow users to view this data from a mobile app.

*This application was started as a Computer Science Senior Capstone Project by Callahan Hirrel at [Hendrix College](https://www.hendrix.edu)*

## Installing 

To install and work on this application, simply clone the repository and install the dependencies. You can use `pip` for the latter. From the application root directory, use the command
```
pip install -r requirements.txt
```

## Running

You can run the application in one of two ways. The simpler is to navigate to the application root directory, then use the command
```
python run.py
```
Alternatively, if you are using virtual environments, from within your virtual environment, set the `FLASK_APP` environment variable to the `src` directory:
```
export FLASK_APP=src
```
Then, use
```
flask run
```
Note, that using `flask run` will not run the application in debug mode. To do this, use
```
FLASK_DEBUG=1 flask run
```
