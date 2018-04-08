"""
    Domain Monitor
    ~~~~~~~~~~~~~

    Our application.

    This is where we bootstrap our Flask application and it's dependencies.

    File name: app.py
    Authors: Richard West, Meg Williamson
    Python Version: 3.6
"""

import click
import csv
import emoji
from flask import Flask
from peewee import *
from domain_monitor import *
from terminaltables import AsciiTable
from models import db, Firm, DomainReport

app = Flask(__name__)

app.config.from_envvar('APP_CONFIG')

# connect to database
db.connect(reuse_if_open=True)

set_common_name_endings(app.config['COMMON_NAME_ENDINGS'])

set_business_entity_endings(app.config['BUSINESS_ENTITY_ENDINGS'])

set_tlds(app.config['TLDS'])

# create the tables. By default, Peewee will determine if the tables already exist, and conditionally create them
db.create_tables([Firm, DomainReport])


@app.cli.command(name='import')
def import_clc_firms():
    """Simple command parses data from Council for Licensed Conveyancers (CLC) firms and inserts into database table."""

    filename = 'raw-firm-data.csv'
    with open(filename, newline='', mode='r') as f:
        # skip the first entry as just column headers
        reader = csv.reader(f)
        next(reader)
        with click.progressbar(reader, length=15900) as bar:
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
        click.echo(emoji.emojize('CLC firms imported successfully :thumbs_up:', use_aliases=True))


@app.cli.command(name='check')
@click.option('--limit', default=None, help='The number of random firms to check')
def check_all_domains(limit):
    """This command takes all, or a given number of, firms, generates variations for them, and attempts to resolve.
    The core functionality of the Domain Monitor program.
    """

    if limit is not None:
        # select some random firms.
        # Postgresql and Sqlite use the 'Random' function, MySQL uses 'Rand'
        firms = Firm.select().order_by(fn.Random()).limit(int(limit))
    else:
        # select all firms
        firms = Firm.select()

    with click.progressbar(firms) as bar:
        click.echo(emoji.emojize(' Checking domains. :hourglass_flowing_sand: '
                                 'Please be patient...we have a lot of domain variations to check!',
                                 use_aliases=True))
        check_domains(bar)

    click.echo(emoji.emojize('All domain variations have been checked :smiley:.\n'
                             'To view the latest domain report, run the following command:\n'
                             ':snake:  ',
                             use_aliases=True) + click.style('flask report', fg='green'))


@app.cli.command(name='report')
def domain_report():
    """Command that generates a tabular report using data from the latest run of check-domains."""

    # get most recent domain report entry
    latest_entry = DomainReport.select().order_by(DomainReport.id.desc()).get()

    # select all reports last checked on the same day as the latest entry
    reports = DomainReport.select().where(DomainReport.last_checked_at >= latest_entry.last_checked_at)

    table_data = [
        # table heading's
        ['Firm Name', 'Known Domain', 'Identified Domain Variation', 'Last Checked'],
    ]

    # loop each report and append respective rows in order to construct table
    for report in reports:
        table_data.append([report.firm.firm_name, report.firm.known_domain, report.domain, report.last_checked_at])

    click.echo(AsciiTable(table_data).table)
