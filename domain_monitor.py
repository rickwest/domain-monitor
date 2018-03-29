import requests
import re

common_name_endings = []


def set_common_name_endings(endings):
    print(endings)
    common_name_endings = endings
    # get the variations from a config file, means we can have different version for dev and prod


print(common_name_endings)


# yield results instead of storing in a massive set?
def generate_variations_from_firm_name(firm_name):
    """

    :param firm_name:
    :return:
    """
    variations = set({})

    # First we need to stem the firm name, removing the common endings
    firm_name = remove_common_name_ending_from_firm_name(firm_name)

    # anything that other than a-z, 0-9 or '-' isn't allowed in a domain name
    regex = r"[^0-9a-z-]"

    # create a version of the firm name with spaces stripped
    # add to set
    firm_name_without_spaces = re.sub(regex, '', firm_name)
    variations.add(firm_name_without_spaces)

    # create a version of the firm name with spaces replaced with hyphens
    # add to set
    firm_name_with_hyphens = re.sub(regex, '-', firm_name)
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


COMMON_TLDS = ['.com', '.co.uk', '.org', '.net', '.uk']


def attempt_domain_resolution(variation):
    for tld in COMMON_TLDS:
        for prefix in ['', 'www.']:
            domain_name = '{prefix}{variation}{tld}'.format(prefix=prefix, variation=variation, tld=tld)
            try:
                # may need to handle redirects differently in the future but set allow to false for now
                r = requests.get('http://{}'.format(domain_name), timeout=2, allow_redirects=False)
            except requests.exceptions.RequestException as e:
                # catch exception and try again with 'www' sub domain
                # do something
                pass
            else:
                print(r.url)


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
    # if not, just return the firm name
    for ending in COMMON_NAME_ENDINGS:
        if firm_name.endswith(ending):
            start_index = firm_name.rfind(ending)
            return firm_name[:start_index].rstrip()
    return firm_name

