import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive.file',
    'https://www.googleapis.com/auth/drive'
]

creds = ServiceAccountCredentials.from_json_keyfile_name('creds.json', scope)
client = gspread.authorize(creds)

ppl = client.open("Workout Log").worksheet("PPL")
test_sheet = client.open('Workout Log').sheet1

test_cell = test_sheet.cell(1, 1).value

print(test_cell)
