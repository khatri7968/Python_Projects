import pandas as pd

def read_excel_sheets(file_path, sheet_names):
    excel_data = {}

    # Read each sheet separately
    for sheet_name in sheet_names:
        excel_data[sheet_name] = pd.read_excel(file_path, sheet_name=sheet_name)
    return excel_data


if __name__ == "__main__":
    file_path = 'MSFT_Project1.xlsx'  # Replace with the path to your Excel file
    sheet_names = ['MSFT', 'Tesla', 'Apple', 'SP500', 'combined']

    excel_data = read_excel_sheets(file_path, sheet_names)

    # Assign DataFrames to variables
    msft_df = excel_data['MSFT']
    tesla_df = excel_data['Tesla']
    apple_df = excel_data['Apple']
    sp500_df = excel_data['SP500']
    combined_df = excel_data['combined']

    # Print DataFrames
    print(msft_df)
