import pandas as pd
import io
from http.server import BaseHTTPRequestHandler
import unittest
import re
from dateutil import parser

def transform_row(row):
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    dob_str = row.get('Date of Birth', '')
    if dob_str:
        dob = parser.parse(dob_str)
        dob = dob.strftime('%d/%m/%Y')
    else:
        dob = ''

    review_str = row.get('Review Date', '')
    if review_str:
        review_date = parser.parse(review_str)
        review_date = review_date.strftime('%d/%m/%Y')
    else:
        review_date = ''

    mob_no = str(row.get('Mobile', ))
    if mob_no and len(mob_no) >= 8:
        mobile = mob_no[-8:]  # Get last 8 digits of mobile number
    else:
        mobile = ''

    # Validate and transform each field of the row
    transformed_row = {
        'Type': row.get('Type', ''),
        'First Name': row.get('First Name', ''),
        'Last Name': row.get('Last Name', ''),
        'Email': row.get('Email', ''),
        'Country Code': row.get('Country Code', ''),
        'Mobile': mobile,
        'Gender': row.get('Gender', ''),
        'Date of Birth': dob,
        'Referrer Email': row.get('Referrer Email', ''),
        'Referrer Relationship': row.get('Referrer Relationship', ''),
        'Source': row.get('Source', 'other'),
        'Smoking Habit': row.get('Smoking Habit', ''),
        'Marital Status': row.get('Marital Status', ''),
        'Postal Code': row.get('Postal Code', ''),
        'Address': row.get('Address', ''),
        'Review Date': review_date,
        'Category': row.get('Category', ''),
        'Note 1': row.get('Note 1', ''),
        'Note 2': row.get('Note 2', ''),
        'Note 3': row.get('Note 3', ''),
        'Note 4': row.get('Note 4', ''),
        'Note 5': row.get('Note 5', '')
    }

    validation_functions = {
        'Type': lambda value: value in ['L', 'A', 'M', 'C'] or value == '',
        'First Name': lambda value: isinstance(value, str) and all(
            c.isalnum() or c.isspace() or c in '/-@' for c in value),
        'Last Name': lambda value: isinstance(value, str) and (
                    all(c.isalnum() or c.isspace() or c in '/-@' for c in value) or value == " "),
        'Email': lambda value: isinstance(value, str) and re.match(email_regex, value),
        'Country Code': lambda value: isinstance(value, str) and value.isdigit() or value == '',
        'Mobile': lambda value: isinstance(value, str) and value.isdigit() and len(value) == 8,
        'Gender': lambda value: isinstance(value, str) and value in ['male', 'female'],
        'Date of Birth': lambda value: isinstance(value, str) and len(value) == 10 and value[2] == '/' and value[
            5] == '/' and value[:2].isdigit() and value[3:5].isdigit() and value[6:].isdigit(),
        'Referrer Email': lambda value: isinstance(value, str) and ('@' in value and '.' in value or value == ''),
        'Referrer Relationship': lambda value: value in ['frined', 'partner', 'parent', 'sibling', 'spouse', 'child',
                                                         'relative', 'colleague', 'other'] or value == '',
        'Source': lambda value: value in ['referral', 'warm', 'telemarketing', 'roadshows', 'seminars', 'stray',
                                          'other'] or value == '',
        'Smoking Habit': lambda value: value in ['yes', 'no'] or value == '',
        'Marital Status': lambda value: value in ['married', 'single', 'divorced', 'widow'] or value == '',
        'Postal Code': lambda value: isinstance(value, str) and value.isdigit() or value == '',
        'Address': lambda value: isinstance(value, str) and all(
            c.isalnum() or c.isspace() or c in ',/-@#:.' for c in value),
        'Review Date': lambda value: isinstance(value, str) and (
                    len(value) == 10 and value[2] == '/' and value[5] == '/' and value[:2].isdigit() and value[
                                                                                                         3:5].isdigit() and value[
                                                                                                                            6:].isdigit() and value <= '31/12/9999') or value == '',
        'Category': lambda value: value in ['A', 'B', 'C', 'D'] or value == '',
        'Note 1': lambda value: isinstance(value, str),
        'Note 2': lambda value: isinstance(value, str),
        'Note 3': lambda value: isinstance(value, str),
        'Note 4': lambda value: isinstance(value, str),
        'Note 5': lambda value: isinstance(value, str)
    }

    for key, value in transformed_row.items():
        if key in validation_functions:
            validation_function = validation_functions[key]
            is_valid = validation_function(value)
            if not is_valid:
                transformed_row[key] = "Error invalid, " + key
    return transformed_row

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            if self.path == '/contacts-nexus-merlin':
                self.send_response(200)
                self.send_header('Content-type', 'text/plain')
                self.end_headers()
                self.wfile.write('Preparing contacts from Nexus to Merlin'.encode('utf-8'))
        except Exception as e:
            self.send_error(500, str(e))

    def do_POST(self):
        try:
            if self.path == '/contacts-nexus-merlin':
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

# Class for testing the code
class TestTransformRow(unittest.TestCase):
    def test_transform_row_valid(self):
        # Test with valid input
        input_data = {'Type': 'C', 'First Name': 'John', 'Last Name': 'Doe',
                      'Email': 'johndoe@example.com', 'Country Code': '',
                      'Mobile': '1234567890', 'Gender': 'male', 'Date of Birth': '23-01-2023',
                      'Referrer Email': '', 'Referrer Relationship': '',
                      'Source': 'other', 'Smoking Habit': 'no', 'Marital Status': '',
                      'Postal Code': '12345', 'Address': 'k Bahru, Unit NO:  11-319', 'Review Date': '23/01/2023',
                      'Category': 'A', 'Note 1': '', 'Note 2': '',
                      'Note 3': '', 'Note 4': '', 'Note 5': ''}
        expected_output = {'Type': 'C', 'First Name': 'John', 'Last Name': 'Doe',
                           'Email': 'johndoe@example.com', 'Country Code': '',
                           'Mobile': '34567890', 'Gender': 'male', 'Date of Birth': '23/01/2023',
                           'Referrer Email': '', 'Referrer Relationship': '',
                           'Source': 'other', 'Smoking Habit': 'no', 'Marital Status': '',
                           'Postal Code': '12345', 'Address': 'k Bahru, Unit NO:  11-319', 'Review Date': '23/01/2023',
                           'Category': 'A', 'Note 1': '', 'Note 2': '',
                           'Note 3': '', 'Note 4': '', 'Note 5': ''}
        self.maxDiff = None
        self.assertEqual(transform_row(input_data), expected_output)
    def test_transform_row_invalid(self):
        # Test with valid input
        input_data = {'Type': 'A', 'First Name': 'akfk.com', 'Last Name': 'Doe',
                      'Email': 'johndoeexample.com', 'Country Code': '',
                      'Mobile': '67a890', 'Gender': 'mle', 'Date of Birth': '',
                      'Referrer Email': '', 'Referrer Relationship': '',
                      'Source': 'other', 'Smoking Habit': 'no', 'Marital Status': '',
                      'Postal Code': '12345', 'Address': 'k Bahru, Unit NO:  11-319', 'Review Date': '',
                      'Category': 'A', 'Note 1': '', 'Note 2': '',
                      'Note 3': '', 'Note 4': '', 'Note 5': ''}
        expected_output = {'Type': 'A', 'First Name': 'Error invalid, First Name', 'Last Name': 'Doe',
                           'Email': 'Error invalid, Email', 'Country Code': '', 'Mobile': 'Error invalid, Mobile',
                           'Gender': 'Error invalid, Gender', 'Date of Birth': 'Error invalid, Date of Birth',
                           'Referrer Email': '', 'Referrer Relationship': '',
                           'Source': 'other', 'Smoking Habit': 'no', 'Marital Status': '',
                           'Postal Code': '12345', 'Address': 'k Bahru, Unit NO:  11-319', 'Review Date': '',
                           'Category': 'A', 'Note 1': '', 'Note 2': '',
                           'Note 3': '', 'Note 4': '', 'Note 5': ''}
        self.maxDiff = None
        self.assertEqual(transform_row(input_data), expected_output)
if __name__ == '__main__':
    unittest.main()