'''
Module for CLI user interaction
'''

# Imports
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

    def bind_keys(pairs_list = None):
        '''
        Bind keys to functions.
        Functions are activated according to user input.
        '''
        # Validate Data
        child_validator = lambda child: helper.is_tuple(child) and len(child) == 2
        are_children_valid = lambda: helper.are_list_children(pairs_list, child_validator)
        is_container_valid = lambda: helper.is_list(pairs_list)
        valid_data =  is_container_valid() and are_children_valid()
        behaviour_loaded = lambda: print('Warning, keys are not bound to functions.')

        if valid_data:
            def display_choices():
                for choice_number, response_pair in enumerate(pairs_list):
                    response_name = response_pair[0]
                    print(f'[{choice_number}] {response_name} ')

            def activate_response(user_input):
                try:
                    choice_number = int(user_input)
                    response_pair = pairs_list[choice_number]
                    response_func = response_pair[1]
                    response_func()
                except (IndexError, TypeError, ValueError):
                    print('\nChoice not found, please try again...\n')
                    wait_for_keypress()

            def wait_for_keypress():
                display_choices()
                user_input = input('\nEnter choice number >>> ')
                activate_response(user_input)

            behaviour_loaded = wait_for_keypress

        return behaviour_loaded

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
