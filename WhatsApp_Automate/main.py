from selenium import webdriver
import time
import csv

# Path to your Chrome WebDriver executable
webdriver_path = 'path/to/chromedriver'

# Path to your CSV file
csv_file_path = 'path/to/contacts.csv'

# Custom message to be sent
custom_message = 'Your personalized message goes here.'

# List of contacts to exclude from receiving the message
exceptions = ['John Doe', 'Jane Smith']

# Load CSV file and retrieve contacts
contacts = []
with open(csv_file_path, 'r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        contacts.append(row)

# Start Selenium WebDriver
driver = webdriver.Chrome(webdriver_path)
driver.get('https://web.whatsapp.com')

# Wait for user to scan QR code and log in to WhatsApp Web manually
input('Press Enter after logging in to WhatsApp Web...')

# Function to check if a contact exists on WhatsApp
def contact_exists(contact_name):
    try:
        driver.find_element_by_xpath(f"//span[@title='{contact_name}']")
        return True
    except:
        return False

# Remove contacts not on WhatsApp
contacts_on_whatsapp = []
for contact in contacts:
    if contact_exists(contact['name']):
        contacts_on_whatsapp.append(contact)

# Send personalized messages
for contact in contacts_on_whatsapp:
    if contact['name'] not in exceptions:
        # Open chat with the contact
        driver.find_element_by_xpath(f"//span[@title='{contact['name']}']").click()
        time.sleep(2)

        # Send the message
        input_box = driver.find_element_by_xpath('//div[@contenteditable="true"][@data-tab="1"]')
        input_box.send_keys(custom_message)
        driver.find_element_by_xpath('//button[@class="_4sWnG"]').click()

        # Wait before sending the next message
        time.sleep(12)

# Close the browser
driver.quit()
