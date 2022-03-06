'''
Module for data manipulation and storage.
'''

# Imports
import time
from datetime import datetime
from google.oauth2.service_account import Credentials
import gspread

# External Database
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')

SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
EXT_DATABASE = GSPREAD_CLIENT.open('clj_database')

JOURNAL_ENTRIES = EXT_DATABASE.worksheet('journal_entries')

# Data Types
INT_DATABASE = []
DATA_TITLES = ['ID', 'DATETIME', 'TEXT']

class JournalEntry:
    '''
    Creates journal entry instances.
    '''
    # Private variables
    _timestamp = None
    _text = ""

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
        Sets private timestamp property.
        '''
        self._timestamp = new_timestamp if isinstance(new_timestamp, float) else time.time()

    @property
    def date(self):
        '''
        Returns private date property i.e. read only.
        '''
        return datetime.date(self._timestamp)

    @property
    def time(self):
        '''
        Returns private time property i.e. read only.
        '''
        return datetime.time(self._timestamp)

    def display(self):
        '''
        Prints details of journal entry.
        '''
        description = f'{self.date} {self.time} >>> {self.text}'
        print(description)

# CRUD Operations
def create_entry(text):
    '''
    Adds new journal entry to INT_DATABASE.
    '''
    new_entry = JournalEntry(text)
    INT_DATABASE.append(new_entry) # convert to google sheets API

def get_entry(index):
    '''
    Retrieves existing journal entry.
    '''

    return INT_DATABASE[index]

def update_entry(index, text):
    '''
    Updates existing journal entry.
    '''
    INT_DATABASE[index].text = text

def delete_entry(index):
    '''
    Deletes existing journal entry.
    '''
    INT_DATABASE.pop(index)
