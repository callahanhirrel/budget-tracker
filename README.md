# BiRT: Budgets in Real Time

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

Before installing, I recommend activating a [virtual environment](https://pythontips.com/2013/07/30/what-is-virtualenv/) of some sort, solely for this application. The virtual environment tool I use is called [`virtualenv`](https://virtualenv.pypa.io/en/latest/), which can be installed with `pip install virtualenv`. Then, you can create and activate your virtual environment with
```
$ virtualenv environment_name
$ source environment_name/bin/activate
```
Then, you can deactivate the virtual enironment with
```
$ deactivate
```

Once you have a virtual environment installed, you can install and work on this application. To do so, simply clone the repository and run the `src/setup.py` script:
```
$ python setup.py install
```
or
```
$ python setup.py develop
```

## Running

You can run the application in one of two ways. The simpler method is to navigate to the application root directory, then use the command
```
$ python run.py
```
This will run the application as a Python module instead of a Flask application. It is easier for development, in my opinion.

Alternatively, if you are using virtual environments, from within your virtual environment, set the `FLASK_APP` environment variable to the `src` directory:
```
$ export FLASK_APP=budget_app
```
Then, use
```
$ flask run
```
Note, that using `flask run` will not run the application in debug mode. To do this, use
```
$ FLASK_DEBUG=1 flask run
```
