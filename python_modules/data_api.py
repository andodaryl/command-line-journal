'''
Module for data manipulation and storage.
'''

# Imports
from datetime import datetime

# Data Types
database = [] #remove once google sheets is fixed

class JournalEntry:
    '''
    Creates journal entry instances.
    '''
    # Private variables
    _timestamp = None
    _text = ""

    def __init__(self, text, timestamp = datetime.today()):
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
        self._timestamp = new_timestamp

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
    Adds new journal entry to database.
    '''
    new_entry = JournalEntry(text)
    database.append(new_entry) # convert to google sheets API

def get_entry(index):
    '''
    Retrieves existing journal entry.
    '''

    return database[index]

def update_entry(index, text):
    '''
    Updates existing journal entry.
    '''
    if int(index): # convert to google sheets API
        database[index].text = text

def delete_entry(index):
    '''
    Deletes existing journal entry.
    '''
    if int(index): # convert to google sheets API
        database.pop(index)
        