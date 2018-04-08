# Domain Monitor

## Why Domain Monitor?

Cyber attacks, specifically in the form of, Phishing and Pharming, Social Engineering type attacks, are becoming increasingly prolific within the UK Legal industry.

In some cases, these attacks have resulted in families losing their life savings, as well as law firms losing thousands of pounds in potential revenue.

For example, scammers will register a domain similar to that of a genuine law firm domain and put up a fake website or a clone of the actual genuine firm website. 
They will then attempt to redirect traffic to the fake website either via exploitation of vulnerabilities in DNS server software, or through Phishing emails to potential targets. 
These targets, often include, but are not limited to people who may in the process of completing a property transaction as in [this example]('https://www.telegraph.co.uk/personal-banking/savings/latest-bank-transfer-fraud-victims-lost-113665-now-homeless/').   

A list of recently identified fraudulent activity can be found on the [Solicitors Regulation Authority(SRA) Scam Alert Page](https://www.sra.org.uk/consumers/scam-alerts/scam-alerts.page).

## Our solution

We decided that we would write a command line application (for now anyway!) in Python, using the Flask framework, in order to try and identify possible fraudulent domain names and websites.

In short, Domain Monitor works by taking a genuine law firm name and producing multiple possible domain name variations of that name. 
We then attempt to resolve each variation in the hope that we can identify a potential scam as early as possible and report to the relevant governing body should it be necessary. 

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


## Installing Domain Monitor and its dependencies

To get started with Domain Monitor, you can either download the source or clone the project using git: 

```commandline
git clone https://rickwest@bitbucket.org/rickwest/domainmonitor.git
```

Following installation, you need to navigate into the project directory and run the following command, in order to install all the projects dependencies:

```commandline
pipenv install
```  

With all the dependencies installed, next activate the virtual environment:

```commandline
pipenv shell
```

*If using PyCharm, make sure that it is using the correct python interpreter for the program. Go to: File->Default Settings->Project Interpreter and select the correct virtual environment from the dropdown. 

## Application config

Because Domain Monitor is a Flask application, you need to tell your terminal the application to work with by exporting the FLASK_APP environment variable. In the case of this application, you do this using the command: 

```commandline
export FLASK_APP=app.py
```

You must also export an environment variable to tell Flask which config file to use. For brevity I recommend running the dev config as this only generates a subset of actual possible variations, rather than the considerably larger amount that is generated in production!
If you do want to use the production config, you had better clear your diary for the rest of the day, so, assuming common sense has prevailed, run:
  
```commandline
export APP_CONFIG=config_dev.py
```

Boom! Your all set! However, should you encounter any problems, please don't hesitate to [email me](mailto:richard.west2@student.shu.ac.uk). Now, on to the easy part...


## Using Domain Monitor


Interacting with Domain Monitor simply entails the use of several simple commands.

To see a list of these commands and a brief description, you can simply run:

```commandline
flask
```

As well as the standard flask commands, you should also see our 3 custom commands, 'check', 'import' and 'report'. You can get more information about each of these commands and any required arguments by adding the '--help' flag. For example:
 
```commandline
flask check --help
```

Now that you are familiar with Domain Monitor, lets get started, and put it to use! 

The first command that needs to be run parses a CSV, containing genuine law firm data, and inserts it into a database table. Run the following:

```commandline
flask import
```

Now we have some data to work with, we need to start generating some possible domain name variations and try to resolve them.
 
By default, the check command will generate variations and check ALL the firms in the database (approximately 12,000) so as you can imagine this can take quite a while to run. As a result, we have added a 'limit' argument which allows you to choose a specific number of random firms rather than running the program for the entire dataset.
I would suggest running the command below, which limits the selection to 15 firms, and this should execute in about 5 minutes. 

```commandline
flask check --limit=15
```
         
The final command should be fairly self explanatory as you will have been prompted by the check command. Running the following, simply shows a table of results from the latest domain 'check'. 

```commandline
flask report
```       

## Running the tests

Domain Monitor also has some tests that ensure the correct generation of expected domain name variations as well as the successful attempt or fail of the variation resolution. You can run the tests by executing the following:

```commandline
python tests.py
```

## Final Note

All being well, and I have every faith, you have managed to run and interact with this small program successfully. It's still very limited in scope and very much a first iteration but something that we will continue to improve and develop.
Hopefully it has demonstrated a good level of understanding and research in to new technologies, that we have managed to successfully apply to a real world problem!

We've thoroughly enjoyed the module, thank you :-)     