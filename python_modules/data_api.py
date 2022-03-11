"""
Module for data manipulation and storage.
"""

# Imports
import time
from datetime import datetime
from google.oauth2.service_account import Credentials
import gspread
from python_modules.helper_api import helper_api as helper


def _get_data_api():
    """
    Data API namespace
    """
    # Helper Functions
    def is_valid_identity(num):
        return num.isdigit() if isinstance(num, str) else isinstance(num, int)

    def is_valid_timestamp(num):
        return num.isdigit() if isinstance(num, str) else isinstance(num, int)

    def is_valid_entry_data(data):
        return len(data) == 3 if isinstance(data, list) else False

    # Database initialiser
    def init_database(database_name, worksheet_name, data_titles):
        """
        Loads or creates external database from Google Sheets.
        """
        scope_list = [
            "https://www.googleapis.com/auth/spreadsheets",
            "https://www.googleapis.com/auth/drive.file",
            "https://www.googleapis.com/auth/drive",
        ]

        CREDS = Credentials.from_service_account_file("creds.json")

        scoped_creds = CREDS.with_scopes(scope_list)
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
        database_name="clj_database",
        worksheet_name="journal_entries",
        data_titles=["ID", "TIMESTAMP", "TEXT"],
    )

    class JournalEntry:
        """
        Creates journal entry instances.
        """

        def __init__(self, entry_data=None):
            empty_data = [None, None, None]
            data_is_valid = is_valid_entry_data(entry_data)
            safe_data = entry_data if data_is_valid else empty_data
            identity_given, timestamp_given, text_given = safe_data
            # Private variables
            self._timestamp = 0.0
            self._datetime = None
            self._text = "Empty"
            # Public variables
            self.timestamp = timestamp_given
            self.text = text_given
            self._id = self._get_valid_identity(identity_given, self.timestamp)

        @staticmethod
        def _get_valid_identity(identity, timestamp):
            """
            Returns valid identity from input.
            i.e. incremented integers else autosave string for error handling.
            """
            safe_identity = identity
            if not is_valid_identity(identity):
                try:
                    # Get values of column 1 i.e. IDs
                    id_list = ext_database.col_values(1)
                    safe_id_list = [int(v) for v in id_list if v.isdigit()]
                    # If no valid IDs found start with first
                    if len(safe_id_list) == 0:
                        safe_identity = 1
                    else:
                        # Get highest ID in stack
                        previous_id = max(safe_id_list)
                        safe_identity = previous_id + 1  # Increment
                except gspread.exceptions.GSpreadException:
                    # String ID for error handling
                    safe_identity = "autosave_" + str(timestamp)
            return safe_identity

        @property
        def timestamp(self):
            """
            Returns private date property.
            """
            return self._timestamp

        @timestamp.setter
        def timestamp(self, new_timestamp):
            """
            Sets private timestamp property and datetime equivalent.
            """
            safe = (
                int(new_timestamp)
                if is_valid_timestamp(new_timestamp)
                else int(time.time())
            )
            self._timestamp = safe
            self._datetime = datetime.fromtimestamp(self._timestamp)

        @property
        def text(self):
            """
            Returns private text property.
            """
            return self._text

        @text.setter
        def text(self, new_text):
            """
            Sets private text property.
            """
            try:
                if new_text:
                    self._text = str(new_text)
            except (NameError, UnicodeEncodeError):
                self._text = self._text  # Silent fail to default value

        @property
        def identity(self):
            """
            Returns private id property i.e. read only.
            """
            return self._id

        @property
        def date(self):
            """
            Returns private date property i.e. read only.
            """
            return datetime.date(self._datetime)

        @property
        def time(self):
            """
            Returns private time property i.e. read only.
            """
            return datetime.time(self._datetime)

        @property
        def details(self):
            """
            Return main details of journal entry i.e. read only.
            """
            return f"({self.identity}) {self.date} {self.time} >>> {self.text}"

    # CRUD Operations
    def get_all_data():
        """
        Get all data from database as list of lists.
        """
        return ext_database.get_all_values()

    def replace_all_data(new_database):
        """
        Replace database with new database received as list of lists.
        """
        ext_database.clear()
        ext_database.update("A:C", new_database)

    def get_all_entries():
        """
        Convert database data retrieved to list of JournalEntry instances.
        """
        data_found = get_all_data()
        entries_found = []
        if data_found:
            data_found.pop(0)  # remove titles
            for entry_data in data_found:
                new_journal = JournalEntry(entry_data)
                entries_found.append(new_journal)
                print(entry_data)
        return entries_found

    def create_entry(text, timestamp=None, identity=None):
        """
        Adds new journal entry to ext_database.
        """
        entry = JournalEntry([identity, timestamp, text])  # validate data
        new_entry_data = [entry.identity, entry.timestamp, entry.text]
        database_found = get_all_data()
        new_database = database_found.copy()
        new_database.append(new_entry_data)
        replace_all_data(new_database)

    def get_entry(identity):
        """
        Generate journal entry instance from existing data in database.
        """
        journal_entry = None
        if is_valid_identity(identity):
            data = get_all_data()

            filter_result = filter(lambda v: v[0] == str(identity), data)
            entry_found = next(filter_result, None)
            journal_entry = JournalEntry(entry_found) if entry_found else None
        return journal_entry

    def update_entry(identity, text, timestamp=None):
        """
        Updates existing journal entry.
        """
        if is_valid_identity(identity):
            old_entry = get_entry(identity)
            search_data = [
                str(old_entry.identity),
                str(old_entry.timestamp),
                str(old_entry.text),
            ]
            database_found = get_all_data()
            entry_found = helper.get_index(search_data, database_found)
            # update entry
            if entry_found:
                # validate data
                new_entry = JournalEntry([identity, timestamp, text])
                new_database = database_found.copy()
                new_database[entry_found][1] = new_entry.timestamp
                new_database[entry_found][2] = new_entry.text
                replace_all_data(new_database)

    def delete_entry(identity):
        """
        Deletes existing journal entry.
        """
        if is_valid_identity(identity):
            old_entry = get_entry(identity)
            search_data = [
                str(old_entry.identity),
                str(old_entry.timestamp),
                str(old_entry.text),
            ]
            database_found = get_all_data()
            entry_found = helper.get_index(search_data, database_found)
            # delete entry
            if entry_found:
                new_database = database_found.copy()
                new_database.pop(entry_found)
                replace_all_data(new_database)

    # Public API
    _public_api = {
        "create_entry": create_entry,
        "get_entry": get_entry,
        "get_all_entries": get_all_entries,
        "update_entry": update_entry,
        "delete_entry": delete_entry,
    }

    return helper.namedtuple_from_dict("data_api", _public_api)


data_api = _get_data_api()
