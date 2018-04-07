"""
    Domain Monitor
    ~~~~~~~~~~~~~

    Creates a peewee database instance and defines the model classes

    File name: models.py
    Authors: Richard West, Meg Williamson
    Python Version: 3.6
"""

from datetime import datetime
from peewee import *

# create a peewee database instance -- our models will use this database to
# persist information
db = SqliteDatabase('domain_monitor.db')


# define a base model class that specifies which database to use.
# this way, any subclasses will automatically use the correct database.
class BaseModel(Model):
    class Meta:
        database = db


# create a domain model to specify its fields and represent our domain table declaratively
class Firm(BaseModel):
    firm_name = CharField()
    email_address = CharField(null=True)
    known_domain = CharField(null=True)


class DomainReport(BaseModel):
    domain = CharField()
    severity = CharField(null=True)
    found_at = DateField(default=datetime.now().date())
    last_checked_at = DateField()
    firm = ForeignKeyField(Firm)