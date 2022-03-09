'''
Module for data manipulation and storage.
'''

# Imports
import time
from datetime import datetime
from collections import namedtuple
from google.oauth2.service_account import Credentials
import gspread

def _get_data_api():
    '''
    IIFE for API namespace
    '''
    # Helper Functions
    namedtuple_from_dict = lambda name, dict: namedtuple(name, dict.keys())(*dict.values())
    is_valid_identity = lambda identity: isinstance(identity, float)

    # Database initialiser
    def init_database(database_name, worksheet_name, data_titles):
        '''
        Loads or creates external database from Google Sheets.
        '''
        scope_list = [
            "https://www.googleapis.com/auth/spreadsheets",
            "https://www.googleapis.com/auth/drive.file",
            "https://www.googleapis.com/auth/drive"
            ]

        creds_data = Credentials.from_service_account_file('creds.json')

        scoped_creds = creds_data.with_scopes(scope_list)
        gspread_client = gspread.authorize(scoped_creds)

        # get spreadsheet else create spreadsheet
        database = None
        try:
            database = gspread_client.open(database_name)
        except gspread.exceptions.GSpreadException:
            new_spreadsheet = gspread_client.create(database_name)
            database = new_spreadsheet

        # get worksheet else create worksheet
        journal_entries = None
        try:
            journal_entries = database.worksheet(worksheet_name)
        except gspread.exceptions.GSpreadException:
            database.add_worksheet(worksheet_name, 500, data_titles.length)

        # ensure first row are data titles
        for column, title in enumerate(data_titles):
            safe_column = column + 1
            journal_entries.update_cell(1, safe_column, title)

        return journal_entries

    # Data Types
    ext_database = init_database(
      database_name = 'clj_database',
      worksheet_name = 'journal_entries',
      data_titles = ['ID', 'DATETIME', 'TEXT']
      )

    class JournalEntry:
        '''
        Creates journal entry instances.
        '''

        def __init__(self, text, timestamp = None):
            # Private variables
            self._timestamp = 0.0
            self._datetime = None
            self._text = "Empty"
            # Public variables
            self.timestamp = timestamp
            self.text = str(text)
            # Id Creation >>> incremented integer IDs for stacked entries
            try:
                id_list = ext_database.col_values(1) # Get values of column 1 i.e. IDs
                safe_id_list = [int(val) for val in id_list if val.isdigit()]
                if len(safe_id_list) == 0:
                    self._id = 1
                else:
                    previous_id = max(safe_id_list) # Get highest ID in stack
                    self._id = previous_id + 1 # Increment
            except gspread.exceptions.GSpreadException:
                self._id = 'autosave_' + str(self.timestamp) # String ID for error handling

        @property
        def timestamp(self):
            '''
            Returns private date property.
            '''
            return self._timestamp

        @timestamp.setter
        def timestamp(self, new_timestamp):
            '''
            Sets private timestamp property and datetime equivalent.
            '''
            self._timestamp = new_timestamp if isinstance(new_timestamp, float) else time.time()
            self._datetime = datetime.fromtimestamp(self._timestamp)

        @property
        def text(self):
            '''
            Returns private text property.
            '''
            return self._text

        @text.setter
        def text(self, new_text):
            '''
            Sets private text property.
            '''
            try:
                self._text = str(new_text)
            except (NameError, UnicodeEncodeError):
                self._text = self._text # Silent fail to default value

        @property
        def identity(self):
            '''
            Returns private id property i.e. read only.
            '''
            return self._id

        @property
        def date(self):
            '''
            Returns private date property i.e. read only.
            '''
            return datetime.date(self._datetime)

        @property
        def time(self):
            '''
            Returns private time property i.e. read only.
            '''
            return datetime.time(self._datetime)

        def display(self):
            '''
            Prints details of journal entry.
            '''
            description = f'{self.date} {self.time} >>> {self.text}'
            print(description)

    # CRUD Operations
    def get_all_data():
        '''
        Get all data from database as list of lists.
        '''
        return ext_database.get_all_values()

    def create_entry(text, timestamp = None):
        '''
        Adds new journal entry to ext_database.
        '''
        new_entry = JournalEntry(text, timestamp) # valid data
        new_entry_data = [new_entry.identity, new_entry.timestamp, new_entry.text]
        database_found = ext_database.get_all_values()
        print(f'Old database: {database_found}')
        database_found.append(new_entry_data)
        print(f'Updated database: {database_found}')
        ext_database.update('A:C', database_found)

    def get_entry(identity):
        '''
        Retrieves existing journal entry from database as list.
        '''
        result = None
        if is_valid_identity(identity):
            filter_logic = lambda entry: entry[0] == identity
            data = get_all_data()
            entry_found = filter(filter_logic, data)
            _, timestamp, text = entry_found if entry_found else [None, None, None]
            result = JournalEntry(text, timestamp)
        return result

    def update_entry(index, text):
        '''
        Updates existing journal entry.
        '''
        # Find journal entry row using index ID and update

    def delete_entry(index):
        '''
        Deletes existing journal entry.
        '''
        # Find journal entry row using index ID and delete

    # Public API
    _public_api = {
        'create_entry': create_entry,
        'get_entry': get_entry,
        'update_entry': update_entry,
        'delete_entry': delete_entry,
        'JournalEntry': JournalEntry
    }

    return namedtuple_from_dict('data_api', _public_api)

data_api = _get_data_api()
