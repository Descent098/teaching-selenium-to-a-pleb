from selenium import webdriver # Step 1 import
from time import sleep
import os

# Step 2 instantiate webdriver instance

## Get the path to the webdriver
if os.name == "nt": # windows
    webdriver_path = os.path.join(os.path.dirname(__file__), "chromedriver.exe")
else:
    webdriver_path = "" # Add in binaries and paths for linux/mac

driver = webdriver.Chrome(webdriver_path)

# Step 3 get a webpage
driver.get("https://google.com") 

driver.find_element_by_xpath("//*[text()='Sign in']").click() # Find ANY element where the inner text says 'Sign in' and click it

driver.find_element_by_xpath("//*[@type='email']").send_keys("kieran@canadiancoding.ca") # Send keys to ANY tag that has the type email i.e. <tag type='email'></tag>

driver.find_element_by_xpath("//*[text()='Next']").click() # Find ANY element where the inner text says 'Next' and click it



## Example of using wait to wait for an element to load (this won't work for google since there's a honeypot input field)
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


try:
    element = WebDriverWait(driver, 10).until(# Check for elment for 10 seconds
        EC.presence_of_element_located((By.XPATH, "//*[@type='password']")) # Check for ANY tag with attribute of type='password'
    )
except:
    print("oof") # Element never showed up

sleep(2) # HACK: this is a workaround to avoid the honeypot input tag
driver.find_element_by_xpath("//*[@type='password']").send_keys("kieran@canadiancoding.ca")




################# Details about XPATH's #################

# Layout is //tag[filter]

# //* <-- Match any TAG
# //a <-- Match a tag
# //h2 <-- Match heading 2 tags


# [] <-- Filters
# [text()='Sign in'] < -- filter function
# [@href='https://www.youtube.com/channel/UC1-WbwQ1sAVZ3AVmrXcBwGw'] < -- Attributes

## Example

driver.get("https://kieranwood.ca")
driver.find_element_by_xpath("//*[@href='#candiancoding']").hover().click() # Find any element where the href attribute is #canadiancoding and click it

# This element is hidden when page first loads, the click before this shows it. It will not work unless it is visible in most cases since click() is based on visible elements
driver.find_element_by_xpath("//*[@href='https://www.youtube.com/channel/UC1-WbwQ1sAVZ3AVmrXcBwGw']").click() 


# Step 4 write the rest of your script
while True:
    ...
webdriver.quit()

