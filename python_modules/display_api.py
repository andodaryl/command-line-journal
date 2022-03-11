'''
Module for CLI user display
'''

# Imports
from python_modules.choice_api import choice_api as choice
from python_modules.helper_api import helper_api as helper

def _get_display_api():
    '''
    Namespace for Display API.
    '''
    # Behaviour
    placeholder = choice

    # Public API
    _public_api = {
        'placeholder': placeholder
    }

    return helper.namedtuple_from_dict('display_api', _public_api)

display_api = _get_display_api()
