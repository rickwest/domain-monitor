def generate_variations_from_firm_name(firm_name):
    # First we need to stem the firm name, replacing common endings and swapping out such things as '-, &, etc'
    # Once we have done the stemming we can start generating permutations as required.
    # For example, we have a firm called Venue Solicitors
    # First we want to removed the common ending 'solicitors'.

    common_name_endings = [
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

    # we also want to try all these also with ltd and limited
    # consider plurals


def attempt_domain_resolution(domain_name):
    tlds = ['com', 'co.uk']
    # this function will take each of the generate permutations and try and resolve it
    # making sure to try www version and all common TLDs
