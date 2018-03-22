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

    # create a version of the firm name with spaces stripped
    # add to set
    firm_name_without_spaces = firm_name.replace(' ', '')
    variations.add(firm_name_without_spaces)

    # create a version of the firm name with spaces replaced with hyphens
    # add to set
    firm_name_with_hyphens = firm_name.replace(' ', '-')
    variations.add(firm_name_with_hyphens)

    # add variations with each common name ending appended
    for ending in COMMON_NAME_ENDINGS:
        variations.add(firm_name_without_spaces + ending)
        variations.add(firm_name_with_hyphens + ending)
        variations.add(firm_name_with_hyphens + '-' + ending)

    # consider plurals
    # consider swapping out characters and words such as '&', 'and' etc
    # consider removal words such as 'and' and 'limited' ect
    return variations


COMMON_TLDS = ['.com', '.co.uk', '.org', '.net']


def attempt_domain_resolution(variation):
    for tld in COMMON_TLDS:
        domain_name = '{variation}{tld}'.format(variation=variation, tld='.co.uk')
        try:
            url = 'http://{}'.format(domain_name)
            r = requests.get(url, timeout=1)
            print(r.status_code)
        except requests.exceptions.RequestException as e:
            print(e)
            # catch exception and try again with 'www' sub domain
            try:
                url = 'http://www.{}'.format(domain_name)
                r = requests.get(url, timeout=0.001)
                print('tried:' + url)
            except requests.exceptions.RequestException as e:
                pass

    # this function will take each of the generate permutations and try and resolve it
    # making sure to try www version and all common TLDs


def check_domains(firms):
    # this function pulls everything together by calling the other functions
    for firm in firms:
        # generate the name variations
        generated_variations = generate_variations_from_firm_name(firm.firm_name)
        for variation in generated_variations:
            attempt_domain_resolution(variation)


def get_domain_from_email_address(email_address):
    return email_address.split('@')[1]


def remove_common_name_ending_from_firm_name(firm_name):
    # loop the common name endings and see if the firm name ends with one
    # if it does, we split the firm name at the relevant index and strip whitespace
    for ending in COMMON_NAME_ENDINGS:
        if firm_name.endswith(ending):
            start_index = firm_name.rfind(ending)
            return firm_name[:start_index].rstrip()


def print_url(url):
    print(url)


attempt_domain_resolution('goggle')