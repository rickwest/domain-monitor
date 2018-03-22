# Domain Monitor

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

## Running the tests

Domain Monitor has some tests that ensure the correct generation of expected domain name variations. Run the tests using the following command:

```commandline
python tests.py
```