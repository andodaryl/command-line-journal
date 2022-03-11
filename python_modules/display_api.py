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
    # Config
    _display = dict(
      welcome_msg = 'Welcome to Command Line Journal!\n',
      goodbye_msg = 'See you next time!\n',
    )

    display = helper.namedtuple_from_dict('display', _display)

    # Behaviour
    greet_user = lambda: print(display.welcome_msg)
    farewell_user = lambda: print(display.welcome_msg)

    def exit_behaviour():
        '''
        Behaviour for exiting application.
        '''
        farewell_user()
        exit()

    def go_to_main_menu():
        '''
        Displays main menu.
        '''
        choices = [
          ('Exit', exit_behaviour),
          ('Show All Journals', choice.get_all_entries),
          ('Create Journal', choice.create_entry),
          ('Retrieve Journal', choice.get_entry),
          ('Update Journal', choice.update_entry),
          ('Delete Journal', choice.delete_entry),
        ]

        wait_for_keypress = choice.bind_keys(choices)

        wait_for_keypress()

    # Public API
    _public_api = dict(
        greet_user = greet_user,
        farewell_user = farewell_user,
        go_to_main_menu = go_to_main_menu
    )

    return helper.namedtuple_from_dict('display_api', _public_api)

display_api = _get_display_api()
