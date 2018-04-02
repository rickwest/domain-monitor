import click
import csv
from flask import Flask
from peewee import *
from domain_monitor import *

app = Flask(__name__)
app.config.from_envvar('APP_CONFIG')


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


# connect to database
db.connect(reuse_if_open=True)


set_common_name_endings(app.config['COMMON_NAME_ENDINGS'])

set_business_entity_endings(app.config['BUSINESS_ENTITY_ENDINGS'])

set_tlds(app.config['TLDS'])


# create the tables. By default, Peewee will determine if the tables already exist, and conditionally create them
db.create_tables([Firm])


@app.cli.command()
def import_clc_firms():
    """Simple program that parses data from Council for Licensed Conveyancers list of firms and inserts into database table. """
    filename = 'raw-firm-data.csv'
    with open(filename, newline='', mode='r') as f:
        # skip the first entry as just column headers
        reader = csv.reader(f)
        next(reader)
        with click.progressbar(reader, length=1000) as bar:
            for row in bar:
                if len(row) == 2:
                    firm_name = row[0].lower()
                    email_address = row[1]
                    known_domain = None
                    if email_address is not '':
                        known_domain = get_domain_from_email_address(email_address)
                    Firm.get_or_create(firm_name=firm_name,
                                       email_address=email_address,
                                       defaults={'known_domain': known_domain})
        click.echo('Database seeded successfully')


@app.cli.command()
def check_all_domains():
    firms = Firm.select()

    with click.progressbar(firms) as bar:
        check_domains(bar)
    click.echo('All domains checked successfully')
