'''
Module for CLI user interaction
'''

# Imports
import keyboard
from python_modules.data_api import data_api as data
from python_modules.helper_api import helper_api as helper

def _get_choice_api():
    '''
    Choice API namespace
    '''

    # Behaviours

    def create_entry():
        '''
        Creates journal entry.
        '''
        print('Creating a new journal... ')
        text_given = input('Please enter text >>> ')
        # Needs data validation and user feedback
        data.create_entry(text_given)
        print('Journal created!\n')

    def get_entry():
        '''
        Retrieves journal entry.
        '''
        print('Retrieving an existing journal... ')
        identity_given = input('Please enter journal number >>> ')
        # Needs data validation and user feedback
        journal_found = data.get_entry(identity_given)
        print('Journal found! \n')
        print(f'{journal_found.details}\n')

    def update_entry():
        '''
        Updates journal entry.
        '''
        print('Updating an existing journal... ')
        identity_given = input('Please enter journal number >>> ')
        text_given = input('Please enter new text >>> ')
        # Needs data validation and user feedback
        data.update_entry(identity_given, text_given)
        updated_journal = data.get_entry(identity_given)
        print('Journal updated!\n')
        print(f'{updated_journal.details}\n')

    def delete_entry():
        '''
        Creates journal entry.
        '''
        print('Deleting an existing journal... ')
        identity_given = input('Please enter journal number >>> ')
        # Needs data validation and user feedback
        data.delete_entry(identity_given)
        print('Journal deleted!')

    def bind_keys(key_func_pairs = None):
        '''
        Bind keys to functions and returns function to wait for keypress.
        '''
        next_func = lambda: None

        if key_func_pairs is not None:
            def activate_response(key_detected):
                behaviour_found = key_func_pairs.get(key_detected)
                if behaviour_found:
                    behaviour_found()

            def wait_for_keypress():
                key_pressed = keyboard.read_event(suppress=True)
                activate_response(key_pressed)

            next_func = wait_for_keypress

        return next_func

    # Public API
    _public_api = {
        'bind_keys': bind_keys,
        'create_entry': create_entry,
        'get_entry': get_entry,
        'update_entry': update_entry,
        'delete_entry': delete_entry,
    }

    return helper.namedtuple_from_dict('choice_api', _public_api)

choice_api = _get_choice_api()
