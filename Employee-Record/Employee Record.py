from os import name
import pandas as pd
import csv
from datetime import datetime, timedelta

def calculate_shift_duration(start_time, end_time):
    start = datetime.strptime(start_time, "%m/%d/%Y %I:%M %p")
    end = datetime.strptime(end_time, "%m/%d/%Y %I:%M %p")
    return (end - start).total_seconds() / 3600  # Convert seconds to hours

def process_csv(filename):
    # Open the CSV file
    with open(filename, 'r') as csvfile:
        csvreader = csv.DictReader(csvfile, delimiter='\t')
        for row in csvreader:
            #Name = row['Employee Name']
            position = row['Employee Name']
            start_time = row['Time']
            end_time = row['Time Out']

            # Check conditions
            if start_time and end_time:
                shift_duration = calculate_shift_duration(start_time, end_time)

                if shift_duration > 14:
                    print(f"{name} ({position}) worked for more than 14 hours in a single shift")

if __name__ == "__main__":
    # Provide the path to your CSV file
    df = pd.read_csv(r'C:\Users\Akshay\Downloads\Assignment_Timecard.csv')
   # csv_filename = 'C:\Users\msi\Downloads\Assignment_Timecard.csv'
    #process_csv(csv_filename)
    #process_csv(df)
    print(df)