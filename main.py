from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from datetime import datetime

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://www.theweathernetwork.com/ca/forecasts/pollen/ontario/ottawa")
elem = driver.find_element_by_css_selector(".pollen .allergy-level")
print(elem.text)



with open('data.csv','a') as fd:
    fd.write("\n\""+ datetime.now().strftime("%m/%d/%Y") + "\",\"" +elem.text + "\"")

driver.close()