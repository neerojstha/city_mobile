import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('city-mobile')

def sales():
    """ 
    Collecting sales information from user
    """
    while True:    
        print("Submit your daily sales figure")
        print("sales figure should be 5 digits, separated by commas")
        print("sample: 01,02,03,04,05\n")

        str_data = input("submit your sales figure here:")
        
        sales_sheet = str_data.split(",")

        if validate_data(sales_sheet):
            print("Correct data")
            break

    return sales_sheet
    

def validate_data(values):
    """ 
    converting to integers all the strings, valueError display if
    cann't be changed or not excepted values requirement meet.
    """
    
    try:
        [int(value) for value in values]
        if len(values) != 5:
            raise ValueError(
                f"Exact 5 digits required, you submitted {len(values)}"
            )
    except ValueError as e:
        print(f"Wrong data: {e}, Enter oncemore.\n")
        return False

    return True    

def new_sales(data):
    """ 
    New sales worksheet created after user submitted information
    """
    print("New sales sheet...\n")
    sales_worksheet = SHEET.worksheet('sales')
    sales_worksheet.append_row(data)
    print("New sales sheet created.\n")



data = sales()
sales_sheet = [int(num) for num in data]    
new_sales(sales_sheet)