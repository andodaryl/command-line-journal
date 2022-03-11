"""
Module for CLI user interaction
"""

# Imports
from python_modules.data_api import data_api as data
from python_modules.helper_api import helper_api as helper
import python_modules.display_api as display


def _get_choice_api():
    """
    Choice API namespace
    """

    # Behaviours

    def create_entry():
        """
        Requests user input to create journal entry.
        """
        print("\nCreating a new journal...")
        text_given = input("Please enter text >>> ")
        data.create_entry(text_given)
        print("\nJournal created!\n")

    def get_entry():
        """
        Requests user input to retrieve journal entry based on identity.
        """
        print("\nRetrieving an existing journal... ")

        def attempt_retrieval():
            try:
                user_input = input("Please enter journal number >>> ")
                identity_given = int(user_input)
                journal_found = data.get_entry(identity_given)
                if journal_found:
                    print("\nJournal found!\n")
                    print(f"{journal_found.details}\n")
                else:
                    raise ValueError
            except ValueError:
                print("\nJournal does not exist!")
                display.display_api.try_again(attempt_retrieval)

        attempt_retrieval()

    def get_all_entries():
        """
        Retrieve and print details of all journal entries.
        """

        def attempt_retrieval():
            print("\nRetrieving all existing journals... ")
            try:
                data_found = data.get_all_entries()
                valid_data = helper.is_list(data_found) and len(data_found) > 0
                if valid_data:
                    print("\nJournals found!\n")
                    for journal_found in data_found:
                        print(f"{journal_found.details}\n")
                else:
                    raise ValueError
            except ValueError:
                print("\nNo journals found!")
                display.display_api.try_again(attempt_retrieval)

        attempt_retrieval()

    def update_entry():
        """
        Requests user input to update journal entry.
        """
        print("\nUpdating an existing journal... ")

        def attempt_update():
            try:
                user_input = input("Please enter journal number >>> ")
                identity_given = int(user_input)
                journal_found = data.get_entry(identity_given)
                if journal_found:
                    text_given = input("Please enter new text >>> ")
                    data.update_entry(identity_given, text_given)
                    updated_journal = data.get_entry(identity_given)
                    print("\nJournal updated!\n")
                    print(f"{updated_journal.details}\n")
                else:
                    raise ValueError
            except ValueError:
                print("\nJournal does not exist!")
                display.display_api.try_again(attempt_update)

        attempt_update()

    def delete_entry():
        """
        Requests user input to delete journal entry.
        """
        print("Deleting an existing journal... ")

        def attempt_delete():
            try:
                user_input = input("Please enter journal number >>> ")
                identity_given = int(user_input)

                def is_journal_found():
                    return data.get_entry(identity_given)

                if is_journal_found():
                    data.delete_entry(identity_given)
                    if not is_journal_found():
                        print("\nJournal deleted!\n")
                    else:
                        raise ValueError
                else:
                    raise ValueError
            except ValueError:
                print("\nJournal does not exist!")
                display.display_api.try_again(attempt_delete)

        attempt_delete()

    def bind_keys(pairs_list=None):
        """
        Bind keys to functions.
        Functions are activated according to user input.
        """
        # Validate Data

        def child_validator(child):
            return helper.is_tuple(child) and len(child) == 2

        def are_children_valid():
            return helper.are_list_children(pairs_list, child_validator)

        def is_container_valid():
            return helper.is_list(pairs_list)

        valid_data = is_container_valid() and are_children_valid()

        def behaviour_loaded():
            print("Warning, keys are not bound to functions.")

        if valid_data:

            def display_choices():
                for choice_number, response_pair in enumerate(pairs_list):
                    response_name = response_pair[0]
                    print(f"[{choice_number}] {response_name} ")

            def activate_response(user_input):
                try:
                    choice_number = int(user_input)
                    response_pair = pairs_list[choice_number]
                    response_func = response_pair[1]
                    response_func()
                except (IndexError, TypeError, ValueError):
                    print("\nChoice not found, please try again...\n")
                    wait_for_keypress()

            def wait_for_keypress():
                print("\nPlease choose an action:\n")
                display_choices()
                user_input = input("\nEnter choice number >>> ")
                activate_response(user_input)

            behaviour_loaded = wait_for_keypress

        return behaviour_loaded

    # Public API
    _public_api = {
        "bind_keys": bind_keys,
        "create_entry": create_entry,
        "get_entry": get_entry,
        "update_entry": update_entry,
        "delete_entry": delete_entry,
        "get_all_entries": get_all_entries,
    }

    return helper.namedtuple_from_dict("choice_api", _public_api)


choice_api = _get_choice_api()
