# Domain Monitor

## What is Domain Monitor?

Domain Monitor is a command line application written in Python using the Flask framework.


## Setting up your local environment

To get started with this project and run locally, you will need Python 3.6 and Pip installed.
 
You can check if you have Python, and which version of it, by opening a terminal and running:

```commandline
python --version
```
 
Additionally, you can check that you have Pip installed by running: 

```commandline
pip --version
```

Domain Monitor also uses Pipenv for dependency management. As with Python and Pip, you can check whether you have Pipenv installed by running 

```commandline
pipenv --version
```

If you don't have Pipenv installed, you can install it using Pip:

```commandline
pip install pipenv
```
 
For more information about installing Python, Pip, and Pipenv, you can follow the awesome guides on Kenneth Reitz' [The Hitchhiker's Guide to Python](http://docs.python-guide.org/en/latest/), specifically http://docs.python-guide.org/en/latest/starting/installation/ and
http://docs.python-guide.org/en/latest/dev/virtualenvs/#make-sure-you-ve-got-python-pip/.


## Installing Domain Monitor, its dependencies and running the application

To get started with Domain Monitor, you can either download the source or clone the project using git: 

```commandline
git clone #repo name# 
```

Following installation, you need to navigate into the project directory and run the following command, in order to install all the projects dependencies:

```commandline
pipenv install
```  

With all the dependencies installed, next activate the virtual environment:

```commandline
pipenv shell
```

## Using Domain Monitor

Because Domain Monitor is a Flask application, you need to tell your terminal the application to work with by exporting the FLASK_APP environment variable. In the case of this application, you do this using the command: 

```commandline
export FLASK_APP=app.py
```

You must also export an environment variable to tell Flask which config file to use. I recommend running the 

Boom! Your all set! However, should you encounter any problems, please don't hesitate to [email me](mailto:richard.west2@student.shu.ac.uk)

## Running the tests

Domain Monitor has some tests that ensure the correct generation of expected domain name variations. Run the tests using the following command:

```commandline
python tests.py
```