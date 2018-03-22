import requests

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

    'ltd',
    'limited',

    'llpltd',
    'llcltd',
    'pllpltd',
    'lawltd',
    'lawllltd',
    'practiceltd',
    'legalltd',
    'lawyersltd',
    'lawyerltd',
    'solicitorsltd',
    'solicitorltd',
    'advocatesltd',
    'advocateltd',
    'associatesltd',
    'associateltd',
    'partnersltd',
    'partnerltd',
    'chambersltd',
    'chamberltd',
    'auditltd',
    'chambersllpltd',
    'lawchamberltd',
    'lawchambersltd',
    'lawpracticeltd',
    'lawllpltd',
    'lawllcltd',
    'lawfirmltd',
    'partllpltd',

    'llplimited',
    'llclimited',
    'pllplimited',
    'lawlimited',
    'lawlllimited',
    'practicelimited',
    'legallimited',
    'lawyerslimited',
    'lawyerlimited',
    'solicitorslimited',
    'solicitorlimited',
    'advocateslimited',
    'advocatelimited',
    'associateslimited',
    'associatelimited',
    'partnerslimited',
    'partnerlimited',
    'chamberslimited',
    'chamberlimited',
    'auditlimited',
    'chambersllplimited',
    'lawchamberlimited',
    'lawchamberslimited',
    'lawpracticelimited',
    'lawllplimited',
    'lawllclimited',
    'lawfirmlimited',
    'partllplimited'
]


def generate_variations_from_firm_name(firm_name):
    variations = set({})
    # First we need to stem the firm name, removing the common endings
    firm_name = remove_common_name_ending_from_firm_name(firm_name)

    # strip spaces from firm name
    firm_name_without_spaces = firm_name.replace(' ', '')
    variations.add(firm_name_without_spaces)

    # replace spaces with '-'
    firm_name_with_hyphens = firm_name.replace(' ', '-')
    variations.add(firm_name_with_hyphens)

    # add variations with each common name ending appended
    for ending in COMMON_NAME_ENDINGS:
        variations.add(firm_name_without_spaces + ending)
        variations.add(firm_name_with_hyphens + ending)
        variations.add(firm_name_with_hyphens + '-' + ending)

    # For example, we have a firm called Venue Solicitors
    # First we want to removed the common ending 'solicitors'.
    # we also want to try all these also with ltd and limited
    # consider plurals
    # consider swapping out characters such as '-, &, etc'
    return variations


TLDS = ['.com', '.co.uk']


def attempt_domain_resolution(variation):
    try:
        res = requests.get('http://' + variation + '.co.uk')
        # print(res.status_code)
    except ConnectionError:
        pass

    tlds = ['.com', '.co.uk']
    # this function will take each of the generate permutations and try and resolve it
    # making sure to try www version and all common TLDs

attempt_domain_resolution('google')


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
    # Loop the common name endings and see if the firm name ends with one
    # If it does, we slice the firm name and strip whitespace
    for ending in COMMON_NAME_ENDINGS:
        if firm_name.endswith(ending):
            start_index = firm_name.rfind(ending)
            return firm_name[:start_index].rstrip()
