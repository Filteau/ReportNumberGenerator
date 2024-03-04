import pandas as pd
import os

class ReportCRUD:
    def __init__(self, db_file):
        self.db_file = db_file
        self.load_database()

    def load_database(self):
        # Loads the database from the Excel file or creates a new one if it doesn't exist 
        if os.path.exists(self.db_file):
            print("Database loaded successfully.")
            self.database = pd.read_excel(self.db_file)
        else:
            self.database = pd.DataFrame(columns=['LocationID', 'UserID', 'Date', 'ReportNum'])
            self.database.to_excel(self.db_file, index=False)

    def create_record(self, record):
        # Adds a new record to the database
        self.database = self.database._append(record, ignore_index=True)
        self.database.to_excel(self.db_file, index=False)

    def read_latest_report(self):
        # Reads the most recent report from the database
        if not self.database.empty:
            latest_report = self.database.iloc[-1].to_dict()
            print("Latest report retrieved")
            return latest_report
        else:
            print("Database is empty, no latest report found.")
            return None

    def update_record(self, index, new_data):
        # Updates an existing record in the database
        if index < len(self.database):
            for key, value in new_data.items():
                self.database.at[index, key] = value
            self.database.to_excel(self.db_file, index=False)
            print("Record updated successfully.")
        else:
            print("Index out of range. Record not updated.")

    def delete_record(self, index):
        # Deletes a record from the database
        if index < len(self.database):
            self.database = self.database.drop(index)
            self.database.to_excel(self.db_file, index=False)
            print("Record deleted successfully.")
        else:
            print("Index out of range. Record not deleted.")

    def read_all(self):
        # Reads all records from the database.
        return self.database
