import requests
import openpyxl

# Function to check if a Jenkins server is up
def check_jenkins_status(url):
    try:
        response = requests.get(url)
        # If the status code is 503 or 500, consider the server down
        if response.status_code == 503 or response.status_code == 500:
            return 'Down'
        elif response.status_code == 200:
            return 'Up'
        else:
            return 'Something Else'
    except requests.RequestException as e:
        # If there's any exception (e.g., network error), consider the server down
        return 'Down'

# Path to your Excel file
excel_file_path = 'path/to/your/excel/file.xlsx'

# Load the workbook and select the active sheet
wb = openpyxl.load_workbook(excel_file_path)
sheet = wb.active

# Add a new column header for status if it doesn't exist
status_column = sheet.max_column + 1
sheet.cell(row=1, column=status_column, value='Status')

# Iterate over each row in the sheet (starting from the second row)
for row_index, row in enumerate(sheet.iter_rows(min_row=2, max_col=1), start=2):
    jenkins_url = row[0].value
    if jenkins_url:
        status = check_jenkins_status(jenkins_url)
        # Save the status in the new column
        sheet.cell(row=row_index, column=status_column, value=status)

# Save the workbook
wb.save(excel_file_path)

print("Jenkins server statuses have been checked and updated in the Excel file.")
