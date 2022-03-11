"""
Module for common helper functions
"""

# Imports
from collections import namedtuple


def _get_helper_api():
    """
    Common API namespace
    """

    # Behaviours
    def get_index(target, source):
        """
        Index method with error handling.
        """
        result = None
        try:
            result = source.index(target)
        except (ValueError, TypeError):
            result = None
        return result

    def namedtuple_from_dict(name, dictionary):
        return namedtuple(name, dictionary.keys())(*dictionary.values())

    def is_list(obj):
        return isinstance(obj, list)

    def is_str(obj):
        return isinstance(obj, str)

    def is_tuple(obj):
        return isinstance(obj, tuple)

    def are_list_children(obj, truth_logic):
        return all(truth_logic(child) for child in obj)

    # Public API
    _public_api = {
        "namedtuple_from_dict": namedtuple_from_dict,
        "get_index": get_index,
        "is_list": is_list,
        "is_tuple": is_tuple,
        "is_str": is_str,
        "are_list_children": are_list_children,
    }

    return namedtuple_from_dict("helper_api", _public_api)


helper_api = _get_helper_api()
