"""
    Domain Monitor
    ~~~~~~~~~~~~~

    Implements the unit tests for the application

    File name: tests.py
    Authors: Richard West, Meg Williamson
    Python Version: 3.6
"""

import unittest
from domain_monitor import set_common_name_endings, set_business_entity_endings, generate_variations_from_firm_name
from config_dev import COMMON_NAME_ENDINGS, BUSINESS_ENTITY_ENDINGS


class TestDomainMonitor(unittest.TestCase):
    def test_generation_of_variations(self):
        """ Test generation of domain variations.

        Test case to compare generated variations against our expected list of results.
        By writing the test first, we were able to write and imporve our domain generation algorithm,
        in order to satisfy our desired outcome.
        """

        firm_name = 'venue conveyancing solicitors limited'

        # set common name endings for dev/test environment
        set_common_name_endings(COMMON_NAME_ENDINGS)

        # set business entity endings for dev/test environment
        set_business_entity_endings(BUSINESS_ENTITY_ENDINGS)

        expected_variations = {
            # stemmed name with common ending
            'venueconveyancing',
            'venueconveyancingllp',
            'venueconveyancinglaw',
            'venueconveyancingsolicitors',

            # stemmed name with common ending plus 'ltd'
            'venueconveyancingltd',
            'venueconveyancingllpltd',
            'venueconveyancinglawltd',
            'venueconveyancingsolicitorsltd',

            # stemmed name with common ending plus 'limited'
            'venueconveyancinglimited',
            'venueconveyancingllplimited',
            'venueconveyancinglawlimited',
            'venueconveyancingsolicitorslimited',

            # stemmed name with hyphen separated common ending
            'venueconveyancing-llp',
            'venueconveyancing-law',
            'venueconveyancing-solicitors',

            # stemmed name with hyphen separated common ending plus 'ltd'
            'venueconveyancing-ltd',
            'venueconveyancing-llpltd',
            'venueconveyancing-lawltd',
            'venueconveyancing-solicitorsltd',

            # stemmed name with hyphen separated common ending plus 'limited'
            'venueconveyancing-limited',
            'venueconveyancing-llplimited',
            'venueconveyancing-lawlimited',
            'venueconveyancing-solicitorslimited',

            # stemmed name with hyphen separated common ending plus hyphen separated 'ltd'
            'venueconveyancing-llp-ltd',
            'venueconveyancing-law-ltd',
            'venueconveyancing-solicitors-ltd',

            # stemmed name with hyphen separated common ending plus hyphen separated 'limited'
            'venueconveyancing-llp-limited',
            'venueconveyancing-law-limited',
            'venueconveyancing-solicitors-limited',

            # hyphen separated stemmed name with common ending
            'venue-conveyancing',
            'venue-conveyancingllp',
            'venue-conveyancinglaw',
            'venue-conveyancingsolicitors',

            # hyphen separated stemmed name with common ending plus 'ltd'
            'venue-conveyancingltd',
            'venue-conveyancingllpltd',
            'venue-conveyancinglawltd',
            'venue-conveyancingsolicitorsltd',

            # hyphen separated stemmed name with common ending plus 'limited'
            'venue-conveyancinglimited',
            'venue-conveyancingllplimited',
            'venue-conveyancinglawlimited',
            'venue-conveyancingsolicitorslimited',

            # hyphen separated stemmed name with hyphen separated common ending
            'venue-conveyancing-llp',
            'venue-conveyancing-law',
            'venue-conveyancing-solicitors',

            # hyphen separated stemmed name with hyphen separated common ending plus 'ltd'
            'venue-conveyancing-ltd',
            'venue-conveyancing-llpltd',
            'venue-conveyancing-lawltd',
            'venue-conveyancing-solicitorsltd',

            # hyphen separated stemmed name with hyphen separated common ending plus 'limited'
            'venue-conveyancing-limited',
            'venue-conveyancing-llplimited',
            'venue-conveyancing-lawlimited',
            'venue-conveyancing-solicitorslimited',

            # hyphen separated stemmed name with hyphen separated common ending plus hyphen separated 'ltd'
            'venue-conveyancing-llp-ltd',
            'venue-conveyancing-law-ltd',
            'venue-conveyancing-solicitors-ltd',

            # hyphen separated stemmed name with hyphen separated common ending plus hyphen separated 'limited'
            'venue-conveyancing-llp-limited',
            'venue-conveyancing-law-limited',
            'venue-conveyancing-solicitors-limited',
        }

        generated_variations = set(variation for variation in generate_variations_from_firm_name(firm_name))

        # check that both generated and expected variation sets are the same length
        self.assertEqual(len(expected_variations), len(generated_variations))

        # check that both set's contain identical items
        self.assertSetEqual(expected_variations, generated_variations)

if __name__ == '__main__':
    unittest.main()
