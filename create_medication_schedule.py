import gspread
from llama_index.tools import FunctionTool
from oauth2client.service_account import ServiceAccountCredentials

def upload_to_google_sheets():
    # Define the scope and credentials
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
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

    # Read the CSV file and upload its contents to the worksheet
    with open('medication_schedule.csv', 'r') as file:
        csv_data = file.read()
        print("CSV file read successfully.")
        print(csv_data)
        client.import_csv(spreadsheet.id, data=csv_data)

    print("CSV file uploaded successfully to Google Sheets.")
    
    
upload_to_google_sheets_engine = FunctionTool.from_defaults(
    fn=upload_to_google_sheets,
    name="upload_to_google_sheets",
    description="This tool uploads the medication schedule CSV file to Google Sheets. The file is uploaded to the first worksheet of the 'medication_schedule' spreadsheet."
)
