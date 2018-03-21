import csv
import click
from app import app, Domain
from flask import render_template
from helpers import *


@app.cli.command()
def parse_clc_csv_and_seed_database():
    filename = 'raw-firm-data.csv'
    with open(filename, newline='', mode='r') as f:
        # skip the first entry as just column headers
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            if len(row) == 2:
                firm_name = row[0].lower()
                email_address = row[1]
                known_domain = None
                if email_address is not '':
                    known_domain = get_domain_from_email_address(email_address)
                Domain.get_or_create(firm_name=firm_name,
                                     email_address=email_address,
                                     defaults={'known_domain': known_domain})

    click.echo('Database seeded successfully')


@app.route("/")
def index():
    return render_template('index.html')
