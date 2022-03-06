'''
Module for data manipulation and storage.
'''

# Imports
import time
from datetime import datetime
from google.oauth2.service_account import Credentials
import gspread

def get_data_api():
    '''
    IIFE for API namespace
    '''
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
    EXT_DATABASE = init_database(
      database_name = 'clj_database',
      worksheet_name = 'journal_entries',
      data_titles = ['ID', 'DATETIME', 'TEXT']
      )

    class JournalEntry:
        '''
        Creates journal entry instances.
        '''
        # Private variables
        _timestamp = 0.0
        _datetime = None
        _text = "Empty"

        def __init__(self, text, timestamp = None):
            # id = stack
            self.timestamp = timestamp
            self.text = str(text)

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
    def create_entry(text):
        '''
        Adds new journal entry to EXT_DATABASE.
        '''
        new_entry = JournalEntry(text)
        # Use JournalEntry instance to validate data and create new journal entry row using next index ID for EXT_DATABASE

    def get_entry(index):
        '''
        Retrieves existing journal entry.
        '''
        # Find journal entry row using index ID, create JournalEntry instance to validate data and return contents as list

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
    return {
        create_entry,
        get_entry,
        update_entry,
        delete_entry,
        JournalEntry
    }

DATA_API = get_data_api()
