# from http.server import BaseHTTPRequestHandler

# class handler(BaseHTTPRequestHandler):

#     def do_GET(self):
#         self.send_response(200)
#         self.send_header('Content-type','text/plain')
#         self.end_headers()
#         self.wfile.write('Preparing policies from AllAssured to Merlin'.encode('utf-8'))
    
#     def do_POST(self):
#         self.send_response(200)
#         self.send_header('Content-type', 'text/plain')
#         self.end_headers()
#         content_length = int(self.headers['Content-Length'])
#         post_data = self.rfile.read(content_length)
#         message = 'You sent: {}'.format(post_data.decode('utf-8'))
#         self.wfile.write(message.encode('utf-8'))


import pandas as pd
import io
from datetime import datetime
from http.server import BaseHTTPRequestHandler
import re
import unittest
from dateutil import parser

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        try:
            if self.path == '/policies-allassured-merlin':
                self.send_response(200)
                self.send_header('Content-type', 'text/plain')
                self.end_headers()
                self.wfile.write('Preparing policies from AllAssured to Merlin'.encode('utf-8'))
        except Exception as e:
            self.send_error(500, str(e))

    def do_POST(self):
        try:
            if self.path == '/policies-allassured-merlin':
                content_type = self.headers['Content-Type']
                
                if content_type != 'text/csv':
                    self.send_error(400, 'Expected Content-Type: text/csv')
                    return
                
                content_length = int(self.headers['Content-Length'])
                post_data = self.rfile.read(content_length)
                csv_data = pd.read_csv(io.StringIO(post_data.decode('utf-8')))

                # Define input and output templates
                input_template = ['Type', 'First Name', 'Last Name', 'Email', 'Country Code', 'Mobile', 'Gender',
                                  'Date of Birth', 'Referrer Email', 'Referrer Relationship', 'Source', 'Smoking Habit',
                                  'Marital Status', 'Postal Code', 'Address', 'Review Date', 'Category', 'Note 1',
                                  'Note 2', 'Note 3', 'Note 4', 'Note 5']
                if not all(col in csv_data.columns for col in input_template):
                    self.send_error(400, 'CSV file does not match input template')
                    return
                # Define the CSV writers with the output templates
                complete_data = pd.DataFrame(columns=input_template)
                incomplete_data = pd.DataFrame(columns=input_template)
                # Parse and validate each row of data
                for i, row in csv_data.iterrows():
                    # Validate and transform each row of data
                    my_row = dict(zip(input_template, row.tolist()))
                    transformed_row = transform_row(my_row)
                    if transformed_row:
                        if "Error" in transformed_row.values():
                            # Add the entire row to the incomplete data
                            incomplete_data = incomplete_data.append(list(transformed_row.values()), ignore_index=True)
                        else:
                            # Add the transformed row to the complete data
                            complete_data = complete_data.append(list(transformed_row.values()), ignore_index=True)
                # Return the formatted data as two CSV files for the user to download
                self.send_response(200)
                self.send_header('Content-type', 'text/csv')
                self.send_header('Content-Disposition', 'attachment; filename="complete_data.csv"')
                self.end_headers()
                complete_data.to_csv(self.wfile, index=False)
                self.wfile.write(b'\r\n')
                self.send_response(200)
                self.send_header('Content-type', 'text/csv')
                self.send_header('Content-Disposition', 'attachment; filename="incomplete_data.csv"')
                self.end_headers()
                incomplete_data.to_csv(self.wfile, index=False)
        except Exception as e:
            self.send_error(500, str(e))

def transform_row(row):

    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    pid_str = row.get('Policy Inception Date', '')
    if pid_str:
        pid = parser.parse(pid_str)
        pid = pid.strftime('%d/%m/%Y')
    else:
        pid = ''

    ped_str = row.get('Policy End Date', '')
    if ped_str:
        ped_date = parser.parse(ped_str)
        ped_date = ped_date.strftime('%d/%m/%Y')
    else:
        ped_date = ''

    pmd_str = row.get('Payment End Date', '')
    if pmd_str:
        pmd_date = parser.parse(pmd_str)
        pmd_date = pmd_date.strftime('%d/%m/%Y')
    else:
        pmd_date = ''    

    


    # Validate and transform each field of the row
    transformed_row = {
        'Email': row.get('Email', ''),
        'Policy name': row.get('Policy Name', ''),
        'Policy Type': row.get('Policy Type', ''),
        'Insurer Name': row.get('Insurer Name', ''),
        'Policy No': row.get('Policy No', ''),
        'Premium Amount': row.get('Premium Amount', ''),
        'Interval Type': row.get('Interval Type', ''),
        'Payment Method': row.get('Payment Method', ''),
        'Policy Inception Date': pid,
        'Policy End Date': ped_date,
        'Payment End Date': pmd_date,
        'Death Sum Assured': row.get('Death Sum Assured', ''),
        'TPD Sum Assured': row.get('TPD Sum Assured', ''),
        'CI Sum Assured': row.get('CI Sum Assured', ''),
        'Early CI Sum Assured': row.get('Early CI Sum Assured', ''),
        'Accidental Death Sum Assured': row.get('Accidental Death Sum Assured', ''),
        'Estimated Maturity Value': row.get('Estimated Maturity Value', ''),
        'Hospital Type': row.get('Hospital Type', ''),
        'Annual Claim Limit': row.get('Annual Claim Limit', ''),
        'Insurance Purpose': row.get('Insurance Purpose', ''),
        'Notes': row.get('Notes', '')
    }
    
    # Remove any leading or trailing whitespace from all fields
    # transformed_row = {key: value.strip() for key, value in transformed_row.items()}
    policy_type = ['Endowment', 'ILP',]

    validation_functions = {
        'Email': lambda value: isinstance(value, str) and re.match(email_regex, value),
        'Policy name': lambda value: isinstance(value, str) and all(c.isalnum() or c.isspace() or c in '/-@' for c in value),
        'Policy Type Name': lambda value: value in ['Health', 'Whole Life', 'Accident', 'Endowment', 'ILP', 'Term'],
        'Insurer Name': lambda value: value in ['AIA', 'Singlife with Aviva', 'AXA', 'Etiqa', 'Friends Provident', 'FWD Insurance', 'Great Eastern Life', 'HSBC', 'LIC', 'Manulife', 'Income', 'Old Mutual', 'Prudential', 'Singlife', 'Tokio Marine', 'UOI', 'Utmost', 'Zurich', 'Others'],
        'Policy No': lambda value: isinstance(value, str) and all(c.isalnum() or c.isspace() or c in '/-@' for c in value),
        'Premium Amount': lambda value: value.isdigit(),
        'Interval Type': lambda value: value in ['Monthly', 'Quarterly', 'Half-Yearly', 'Yearly', 'Single'],
        'Payment Method': lambda value: value in ['Cash', 'SRS', 'CPF OA', 'CPF SA', 'CPF MA'],
        'Policy Inception Date': lambda value: isinstance(value, str) and len(value) == 10 and value[2] == '/' and value[5] == '/' and value[:2].isdigit() and value[3:5].isdigit() and value[6:].isdigit(),
        'Policy End Date': lambda value: isinstance(value, str) and len(value) == 10 and value[2] == '/' and value[5] == '/' and value[:2].isdigit() and value[3:5].isdigit() and value[6:8].isdigit() and value[9:].isdigit(),
        'Policy End Date': lambda value: isinstance(value, str) and len(value) == 10 and value[2] == '/' and value[5] == '/' and value[:2].isdigit() and value[3:5].isdigit() and value[6:8].isdigit() and value[9:].isdigit(),
        'Payment End Date': lambda value: isinstance(value, str) and len(value) == 10 and value[2] == '/' and value[5] == '/' and value[:2].isdigit() and value[3:5].isdigit() and value[6:].isdigit(),
        'Death Sum Assured': lambda value: isinstance(value, str) and value.isdigit(),
        'TPD Sum Assured': lambda value: isinstance(value, str) and value.isdigit(),
        'CI Sum Assured': lambda value: isinstance(value, str) and value.isdigit(),
        'Early CI Sum Assured': lambda value: isinstance(value, str) and value.isdigit(),
        'Accidental Death Sum Assured': lambda value: isinstance(value, str) and value.isdigit(),
        'Estimated Maturity Value': lambda value: isinstance(value, str) and value.isdigit(),
        'Hospital Type': lambda value: value in ['Class A', 'Class B1', 'Class B2', 'Class C', 'Private'],
        'Annual Claim Limit': lambda value: isinstance(value, str) and value.isdigit(),
        'Insurance Purpose': lambda value: isinstance(value, str) and value in ['accumulation', 'protection'] if 'Endowment' in policy_type or 'ILP' in policy_type else True,
        'Notes' : lambda value: isinstance(value, str)
    }    
    
    for key, value in transformed_row.items():
        if key in validation_functions:
            validation_function = validation_functions[key]
            is_valid = validation_function(value)
            if not is_valid:
                transformed_row[key] = f"Error invalid, {key}"
    return transformed_row


class TestPolicyHandler(unittest.TestCase):

    def test_transform_row_valid_input(self):
        input_data = {'Email': 'john.doe@example.com', 'Policy Name': 'Life Insurance', 'Policy Type': 'Term', 'Insurer Name': 'Ahmad', 
                      'Policy No': 'POL-1234', 'Premium Amount': '1000', 'Interval Type': 'Monthly', 'Payment Method': 'Cash', 
                      'Policy Inception Date': '2021-01-01', 'Policy End Date': '2031-01-01', 'Payment End Date': '2025-01-01', 
                      'Death Sum Assured': '50000', 'TPD Sum Assured': '0', 'CI Sum Assured': '0', 'Early CI Sum Assured': '0', 
                      'Accidental Death Sum Assured': '0', 'Estimated Maturity Value': '50000', 'Hospital Type': 'Class A', 
                      'Annual Claim Limit': '10000', 'Insurance Purpose': 'Protection', 'Notes': 'Policy is non-transferable'}
        expected_output = {'Email': 'john.doe@example.com', 'Policy Name': 'Life Insurance', 'Policy Type': 'Term', 'Insurer Name': 'Ahmad', 
                      'Policy No': 'POL-1234', 'Premium Amount': '1000', 'Interval Type': 'Monthly', 'Payment Method': 'Cash', 
                      'Policy Inception Date': '01/01/2021', 'Policy End Date': '01/01/2031', 'Payment End Date': '01/01/2025', 
                      'Death Sum Assured': '50000', 'TPD Sum Assured': '0', 'CI Sum Assured': '0', 'Early CI Sum Assured': '0', 
                      'Accidental Death Sum Assured': '0', 'Estimated Maturity Value': '50000', 'Hospital Type': 'Class A', 
                      'Annual Claim Limit': '10000', 'Insurance Purpose': 'Protection', 'Notes': 'Policy is non-transferable'}
        self.maxDiff = None
        self.assertEqual(transform_row(input_data), expected_output)

if __name__ == '__main__':
    unittest.main()