'''
Module for CLI user interaction
'''

# Imports
from data_api import data_api as data
from helper_api import helper_api as helper

def _get_choice_api():
    '''
    Choice API namespace
    '''

    # Behaviours
    placeholder = data

    # Public API
    _public_api = {
        'placeholder': placeholder
    }

    return helper.namedtuple_from_dict('choice_api', _public_api)

choice_api = _get_choice_api()
