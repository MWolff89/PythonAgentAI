import csv
from llama_index.tools import FunctionTool
import os

csv_file = os.path.join("data", "medication_schedule.csv")

def create_csv(header, data):
    # # Sample data to be written to the CSV file
    # header = ['Name', 'Age', 'City']
    # data = [
    #     ['John Doe', '28', 'New York'],
    #     ['Jane Doe', '32', 'Los Angeles'],
    #     ['Jim Brown', '45', 'Chicago']
    # ]
    
    # Writing to the CSV file
    with open(csv_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        
        # Writing the header
        writer.writerow(header)
        
        # Writing the data rows
        for row in data:
            writer.writerow(row)

csv_engine = FunctionTool.from_defaults(
    fn=create_csv,
    name="csv_creator",
    description="This tool creates a CSV file with the given header and data. The file is saved in the data directory. The header and data are passed as arguments to the function. there can only be a maximum of 4 columns accordingly BUT you should only generate as many columns as required. that is, if the maximum number of columns required is 3, then you should only generate 3 columns. if the maximum number of columns required is 2, then you should only generate 2 columns. to be precise, if all the cells of any of the columns are empty, then you should not generate that column."
)
