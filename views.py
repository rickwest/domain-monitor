import csv
import click
from app import app, Firm
from flask import render_template
from domain_monitor import *


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

