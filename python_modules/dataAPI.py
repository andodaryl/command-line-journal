# Imports
from datetime import datetime

# Data Types
database = []

class JournalEntry:
  '''
  Creates journal entry instances.
  '''
  def __init__(self, text):
    today = datetime.today()
    self.date = datetime.date(today)
    self.time = datetime.time(today)
    self.text = text

# CRUD Operations
def create_entry(text):
  '''
  Adds new journal entry to database.
  '''
  new_entry = JournalEntry(text)
  database.append(new_entry)

def get_entry(index):
  '''
  Retrieves existing journal entry.
  '''
  return database[index]

def update_entry(index, text):
  '''
  Updates existing journal entry.
  '''
  database[index].text = text

def delete_entry(index):
  '''
  Deletes existing journal entry.
  '''
  database.pop(index)

# Testing
print('Current database:')
print(database)

print('\nAttempt to create entry... ')
create_entry('First entry')

print('\nAttempt to get entry:')
entry_found = get_entry(0) 
print(f'object: {entry_found}')
print(f'date: {entry_found.date}')
print(f'time: {entry_found.time}')
print(f'text: {entry_found.text}')

print('\nAttempt to update entry:')
update_entry(0, 'New text')
entry_found = get_entry(0) 
print(f'object: {entry_found}')
print(f'date: {entry_found.date}')
print(f'time: {entry_found.time}')
print(f'text: {entry_found.text}')

print('\nAttempt to delete entry...')
delete_entry(0)

print('\nCurrent database:')
print(database)