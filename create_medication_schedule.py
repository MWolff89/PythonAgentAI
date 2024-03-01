import gspread
from llama_index.tools import FunctionTool
from oauth2client.service_account import ServiceAccountCredentials

import gspread
from oauth2client.service_account import ServiceAccountCredentials
import csv

def upload_csv_to_google_sheets():
    # Define the scope and credentials
    scope = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)

    # Authorize the client
    client = gspread.authorize(credentials)
    
    sheet_title = "medication_schedule"

    # Open the desired spreadsheet by its title
    spreadsheet = client.open(sheet_title)

    # Create a new worksheet or access an existing one
    # Here, a new worksheet is added with a title and initial size
    # Adjust the rows and cols numbers based on the size of your CSV data
    try:
        worksheet = spreadsheet.add_worksheet(title="Imported CSV Data", rows="100", cols="20")
    except gspread.exceptions.APIError:
        # If the worksheet already exists, select it instead
        worksheet = spreadsheet.worksheet("Imported CSV Data")
        
    csv_filepath = 'data/medication_schedule.csv'

    # Read the CSV file and prepare data for upload
    with open(csv_filepath, 'r', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file)
        csv_data = list(csv_reader)

    # Update the worksheet with CSV data
    worksheet.update('A1', csv_data)

    print(f"CSV data from {csv_filepath} uploaded successfully to '{sheet_title}'.")

# Example usage
# Replace 'your_csv_file.csv' with the path to your actual CSV file
# Replace 'Your Spreadsheet Title' with the title of your target Google Sheet
# upload_csv_to_google_sheets('your_csv_file.csv', 'Your Spreadsheet Title')

upload_to_google_sheets_engine = FunctionTool.from_defaults(
    fn=upload_csv_to_google_sheets,
    name="upload_csv_to_google_sheets",
    description="This tool uploads the medication schedule CSV file to Google Sheets"
)
