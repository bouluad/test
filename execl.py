import openpyxl
import subprocess

# Load the workbook and select the active sheet
wb = openpyxl.load_workbook('path/to/your/file.xlsx')
sheet = wb.active

# Iterate over each row in the sheet
for row in sheet.iter_rows(min_row=2, values_only=True):  # Assuming the first row is the header
    trigram = row[0]
    iappliid = row[1]
    
    # Construct the curl command
    curl_command = f'curl -X POST "http://your.api.endpoint" -d "trigram={trigram}&iappliid={iappliid}"'
    
    # Execute the curl command
    subprocess.run(curl_command, shell=True)

print("All API calls have been made.")
