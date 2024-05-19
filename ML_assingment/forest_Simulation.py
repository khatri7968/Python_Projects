import pandas as pd


def read_excel_sheets(file_path, sheet_names):
    excel_data = {}

    # Read each sheet separately
    for sheet_name in sheet_names:
        excel_data[sheet_name] = pd.read_excel(file_path, sheet_name=sheet_name)

    return excel_data


def print_excel_data(excel_data):
    # Iterate through each sheet in the Excel file
    for sheet_name, sheet_data in excel_data.items():
        print(f'Sheet name: {sheet_name}')
        print(sheet_data)


if __name__ == "__main__":
    file_path = 'MSFT_Project1.xlsx'  # Replace with the path to your Excel file
    sheet_names = ['MSFT', 'Tesla', 'Apple', 'SP500', 'combined']

    excel_data = read_excel_sheets(file_path, sheet_names)
    print_excel_data(excel_data)
