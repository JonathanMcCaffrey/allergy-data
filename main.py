from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime
import smtplib, ssl
import os
import sys

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.theweathernetwork.com/ca/forecasts/pollen/ontario/ottawa")
elem = driver.find_element_by_css_selector(".pollen .allergy-level")
pollenReport = "\n\""+ datetime.now().strftime("%m/%d/%Y") + "\",\"" +elem.text + "\""
driver.close()
with open('data.csv','a') as fd:
    fd.write(pollenReport)
# Get environment variables
EMAIL = os.getenv('EMAIL')
PASSWORD = os.environ.get('PASSWORD')
smtp_server = "smtp.gmail.com"
port = 587  # For starttls
# Create a secure SSL context
context = ssl.create_default_context()
message = """\
Subject: Pollen Report
""" + pollenReport
# Try to log in to server and send email
try:
    server = smtplib.SMTP(smtp_server,port)
    server.ehlo() # Can be omitted
    server.starttls(context=context) # Secure the connection
    server.ehlo() # Can be omitted
    server.login(EMAIL, PASSWORD)
    # TODO: Send email here
    server.sendmail(EMAIL, EMAIL, message)
except Exception as e:
    # Print any error messages to stdout
    print(e)
finally:
    server.quit() 
    
# calculate stuff
sys.stdout.write(message)
sys.stdout.flush()
sys.exit(0)