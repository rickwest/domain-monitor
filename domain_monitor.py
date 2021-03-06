"""
    Domain Monitor
    ~~~~~~~~~~~~~

    Implements the main application logic associated with generation
    of domain name variations and attempted resolution

    File name: domain_monitor.py
    Authors: Richard West, Meg Williamson
    Python Version: 3.6
"""

import requests
import re
from datetime import datetime
from typing import Iterable
from models import Firm, DomainReport

common_name_endings = []

business_entity_endings = []

common_tlds = []


def set_common_name_endings(endings: Iterable[str]):
    """Sets the value of the global common_name_endings variable.

    Allows us to set the value dependant on environment, making development and testing easier.
    In development and testing, we can use a subset of possible common_name_endings,
    without having to use extensive production config.
    """
    global common_name_endings
    common_name_endings = list(endings)


def set_business_entity_endings(endings: Iterable[str]):
    """Sets the value of the global business_entity_endings variable.

    Allows us to set the value dependant on environment, making development and testing easier.
    In development and testing, we can use a subset of possible business_entity_endings,
    without having to use extensive production config.
    """
    global business_entity_endings
    business_entity_endings = list(endings)


def set_tlds(tlds: Iterable[str]):
    """Sets the value of the global common_tlds variable.

    Allows us to set the value dependant on environment, making development and testing easier.
    In development and testing, we can use a subset of possible common_tlds,
    without having to use extensive production config.
    """
    global common_tlds
    common_tlds = list(tlds)


def generate_variations_from_firm_name(firm_name: str):
    """Generate possible domain name variations based on a firm name
    
    We originally started by defining an empty set, then naively adding multiple variations to that and returning it.
    However, we quickly realised that even with only the basic variations, that we are currently generating,
    these sets would easily contain 250+ variations with the production config. 
    With plans to expand the scope of this program beyond the duration of the university module, 
    by adding numerous other possible variations on names, we did some research and 
    found that by using generators we could improve our application's performance and 
    consume less memory as compared to normal collections.
    """

    # First we need to stem the firm name, removing common endings
    firm_name = stem_firm_name(firm_name)

    # anything that other than a-z, 0-9 or '-' isn't allowed in a domain name
    regex = r"[^0-9a-z-]"

    # create a version of the firm name with spaces stripped
    firm_name_without_spaces = re.sub(regex, '', firm_name)

    # create a version of the firm name with spaces replaced with hyphens
    firm_name_with_hyphens = re.sub(regex, '-', firm_name)

    for name in [firm_name_without_spaces, firm_name_with_hyphens]:
        yield(name)

        for business_entity in business_entity_endings:
            yield('{name}{business_entity}'.format(name=name, business_entity=business_entity))
            yield('{name}-{business_entity}'.format(name=name, business_entity=business_entity))

            for ending in common_name_endings:
                yield('{name}{ending}'.format(name=name, ending=ending))
                yield('{name}-{ending}'.format(name=name, ending=ending))
                yield('{name}{ending}{business_entity}'.format(name=name, ending=ending, business_entity=business_entity))
                yield('{name}-{ending}{business_entity}'.format(name=name, ending=ending, business_entity=business_entity))
                yield('{name}-{ending}-{business_entity}'.format(name=name, ending=ending, business_entity=business_entity))

    # TODO - consider pluralisation of firm names, swapping out characters and words such as '&', 'and' etc


def attempt_domain_resolution(variation):
    """Build a domain from variation and attempt to resolve

    We decided to make a get request, rather than a simple dns lookup, as future plans include scraping and parsing
    the result of the request in order to try an evaluate the contents of the page.
    """
    for tld in common_tlds:
        for prefix in ['', 'www.']:
            domain_name = '{prefix}{variation}{tld}'.format(prefix=prefix, variation=variation, tld=tld)
            try:
                # may need to handle redirects differently in the future but set allow to false for now
                r = requests.get('http://{}'.format(domain_name), timeout=2, allow_redirects=False)
            except requests.exceptions.RequestException as e:
                # catch specific request exception as we may want to handle this in future
                pass
            except:
                # not at all ideal, but we don't want to interrupt program execution
                pass
            else:
                return r


def check_domains(firms: Iterable[Firm]):
    """This is the function that pulls everything together.

    Loops through the Firms iterable, calls the generate_variations_from_firm_name function,
    then loops each variation and tries to resolve by calling the attempt_domain_resolutions function.
    """

    for firm in firms:
        for variation in generate_variations_from_firm_name(firm.firm_name):
            r = attempt_domain_resolution(variation)
            if r:
                # remove 'http://' from start and trailing slash
                domain_name = r.url[7:-1]
                if domain_name != firm.known_domain:
                    DomainReport.get_or_create(domain=domain_name,
                                               defaults={'firm': firm, 'last_checked_at': datetime.now().date()})


def get_domain_from_email_address(email_address: str) -> str:
    """Split an email address on the '@' and returns domain part of it.

    We make the assumption that the argument will always be a genuine email address,
    as it is coming from a trusted source, and thus don't do any checking or validation.
    """
    return email_address.split('@')[1]


def stem_firm_name(firm_name: str) -> str:
    """Does stemming of a firm name.

    Takes a firm name and checks if it ends with a 'business_entity_ending' (e.g. 'limited'), and strips as appropriate.
    Then, checks if the firm name ends with a 'common_name_ending' (e.g. 'solicitors'), and strips that as appropriate,
    and finally returns the stemmed name.
    """

    # loop the business_entity_endings and see if the firm name ends with one,
    # if it does, split the firm name at the relevant index and strip whitespace.
    for ending in business_entity_endings:
        if firm_name.endswith(ending):
            start_index = firm_name.rfind(ending)
            firm_name = firm_name[:start_index].rstrip()

    # loop the common name endings and see if the firm name ends with one
    # if it does, split the firm name at the relevant index and strip whitespace.
    # return the resulting 'stemmed' name.
    for ending in common_name_endings:
        if firm_name.endswith(ending):
            start_index = firm_name.rfind(ending)
            return firm_name[:start_index].rstrip()

    return firm_name
