COMMON_NAME_ENDINGS = [
    'llp',
    'llc',
    'pllp',
    'law',
    'lawll',
    'practice',
    'legal',
    'lawyers',
    'lawyer',
    'solicitors',
    'solicitor',
    'advocates',
    'advocate',
    'associates',
    'associate',
    'partners',
    'partner',
    'chambers',
    'chamber',
    'audit',
    'chambersllp',
    'lawchamber',
    'lawchambers',
    'lawpractice',
    'lawllp',
    'lawllc',
    'lawfirm',
    'partllp',
]


def generate_variations_from_firm_name(firm_name):
    variations = set({})
    # First we need to stem the firm name, removing the common endings
    # To do this we loop through the common name endings and see if the firm name ends with one
    # If it does, we slice the firm name
    firm_name = remove_common_name_ending_from_firm_name(firm_name)
    # strip spaces from firm name
    firm_name = firm_name.replace(' ', '')

    # add basic firm name to set
    variations.add(firm_name)

    # add variations with each common name ending appended
    for ending in COMMON_NAME_ENDINGS:
        variations.add(firm_name + ending)
        variations.add(firm_name + ending + 'limited')
        variations.add(firm_name + ending + 'ltd')

    # For example, we have a firm called Venue Solicitors
    # First we want to removed the common ending 'solicitors'.
    # we also want to try all these also with ltd and limited
    # consider plurals
    # consider swapping out characters such as '-, &, etc'
    return variations


def attempt_domain_resolution(domain_name):
    tlds = ['com', 'co.uk']
    # this function will take each of the generate permutations and try and resolve it
    # making sure to try www version and all common TLDs


def check_domains():
    # this function will pull everything together and call all the other functions
    # fetch each company from database
    for firm in firms:
        domain_variations = generate_variations_from_firm_name(firm.firm_name)
        for variation in domain_variations:
            attempt_domain_resolution(variation)


# helper functions
def get_domain_from_email_address(email_address):
    return email_address.split('@')[1]


def remove_common_name_ending_from_firm_name(firm_name):
    for ending in COMMON_NAME_ENDINGS:
        if firm_name.endswith(ending):
            start_index = firm_name.rfind(ending)
            return firm_name[:start_index]
