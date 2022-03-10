'''
Module for common helper functions
'''

# Imports
from collections import namedtuple

def _get_helper_api():
    '''
    Common API namespace
    '''

    # Behaviours
    def get_index(target, source):
        '''
        Index method with error handling.
        '''
        result = None
        try:
            result = source.index(target)
        except (ValueError, TypeError):
            result = None
        return result

    namedtuple_from_dict = lambda name, dict: namedtuple(name, dict.keys())(*dict.values())

    # Public API
    _public_api = {
      'namedtuple_from_dict': namedtuple_from_dict,
      'get_index': get_index
    }

    return namedtuple_from_dict('helper_api', _public_api)

helper_api = _get_helper_api()
