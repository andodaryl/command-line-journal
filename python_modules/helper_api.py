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

    is_list = lambda obj: isinstance(obj, list)
    is_str = lambda obj: isinstance(obj, str)
    is_tuple = lambda obj: isinstance(obj, tuple)
    are_list_children = lambda obj, truth_logic: all(truth_logic(child) for child in obj)

    # Public API
    _public_api = {
      'namedtuple_from_dict': namedtuple_from_dict,
      'get_index': get_index,
      'is_list': is_list,
      'is_tuple': is_tuple,
      'is_str': is_str,
      'are_list_children': are_list_children
    }

    return namedtuple_from_dict('helper_api', _public_api)

helper_api = _get_helper_api()
