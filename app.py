from flask import Flask
from flask import render_template
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


domains = Domain.select()

for domain in domains:
    print(domain.email_address)


@app.route("/")
def index():
    return render_template('index.html')