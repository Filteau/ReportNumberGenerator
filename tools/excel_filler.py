import pandas as pd
import random
from datetime import datetime, timedelta

# Function to generate random date
def random_date(year, month):
    return datetime(year, month, random.randint(1, 28)).strftime("%m%y")

# Load the existing Excel file
file_name = 'c:/Users/cebel/Desktop/Python/Programming/Proof of Concept/Report Tracking/example_db.xlsx'
df = pd.read_excel(file_name)

# Generate dummy data
for year in range(2022, 2024):
    for month in range(1, 13):
        num_reports = random.randint(1, 24)  # Random number of reports up to 24
        for report_num in range(1, num_reports + 1):
            location_id = random.randint(1, 150)
            user_id = random.randint(1, 500)
            date = random_date(year, month)
            df = df._append({'LocationID': location_id, 'UserID': user_id, 'Date': date, 'ReportNum': report_num}, ignore_index=True)

# Sorting the DataFrame by Date and then by ReportNum
df['YearMonth'] = df['Date'].apply(lambda x: x[-4:])  # Extracts the MMYY format
df['Year'] = df['Date'].apply(lambda x: x[2:])  # Extracts the year part of MMYY
df['Month'] = df['Date'].apply(lambda x: x[:2])  # Extracts the month part of MMYY
df = df.sort_values(by=['Year', 'Month', 'ReportNum'])
df = df.drop(columns=['YearMonth', 'Year', 'Month'])

# Save the updated DataFrame to the Excel file
df.to_excel(file_name, index=False)

print(f'Excel file "{file_name}" has been updated with example data.')








