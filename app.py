from flask import Flask
from peewee import *

app = Flask(__name__)


# create a peewee database instance -- our models will use this database to
# persist information
db = SqliteDatabase('domain_monitor.db')


# define a base model class that specifies which database to use.
# this way, any subclasses will automatically use the correct database.
class BaseModel(Model):
    class Meta:
        database = db


# create a domain model to specifies its fields and represent our domain table declaritively
class Domain(BaseModel):
    firm_name = CharField()
    email_address = CharField()
    domain_name = CharField(null=True, unique=True)


# connect to database and create tables
db.connect(reuse_if_open=True)
db.create_tables([Domain])


# add a couple of sample domains
Domain.create(firm_name='Venue Solicitors', email_address='info@venuesolicitors.co.uk', domain_name=None).save()
Domain.create(firm_name='ABC Law', email_address='hello@abclaw.com', domain_name=None).save()

# A function that takes a name and does the name stemming and generates a list of variations.

# Write a test case to compare returned result against our expected list of results.

# A function that takes each name and tries to resolve it, making sure to try www version and all TLDs.
