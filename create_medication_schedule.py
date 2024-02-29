import gspread
from llama_index.tools import FunctionTool
from oauth2client.service_account import ServiceAccountCredentials

import gspread
from oauth2client.service_account import ServiceAccountCredentials
import csv

def upload_to_google_sheets():
    try:
        # Define the scope and credentials
        scope = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
        credentials = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)

        # Authorize the client
        client = gspread.authorize(credentials)

        print("Client authorized successfully.")
        # print the client
        print(client)

        # Open the desired spreadsheet by its title
        spreadsheet = client.open('medication_schedule')
        print("Spreadsheet opened successfully.")
        print(spreadsheet)

        # Select the worksheet where you want to upload the CSV data
        worksheet = spreadsheet.get_worksheet(0)  # Index 0 represents the first worksheet

        # Read the CSV file and convert its contents to a list of lists
        with open('medication_schedule.csv', 'r') as file:
            csv_reader = csv.reader(file)
            csv_data = list(csv_reader)
            print("CSV file read and processed successfully.")

        # Upload the data to the worksheet
        worksheet.update('A1', csv_data)

        print("CSV file uploaded successfully to Google Sheets.")

    except gspread.exceptions.GSpreadException as e:
        print(f"An error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Remember to call your function to execute it
# upload_to_google_sheets()




upload_to_google_sheets_engine = FunctionTool.from_defaults(
    fn=upload_to_google_sheets,
    name="upload_to_google_sheets",
    description="This tool uploads the medication schedule CSV file to Google Sheets. The file is uploaded to the first worksheet of the 'medication_schedule' spreadsheet."
)
